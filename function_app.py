import azure.functions as func
import logging
import json
import traceback
from datetime import datetime

from app.bronze.validators import validate_event
from app.silver.validators import validate_silver_record
from app.shared.writers import write_event
from app.silver.transformers import transform_to_silver
from app.silver.current_orders import build_current_order
from app.silver.current_order_state import (read_existing_current_order, should_overwrite_current_order)
from app.gold.gold_aggregations import run_gold_batch_for_today

app = func.FunctionApp()

@app.event_hub_message_trigger(
    arg_name="azeventhub",
    event_hub_name="sales-order",
    connection="EVENT_HUB_CONNECTION"
)
def sales_ingest_function(azeventhub: func.EventHubEvent):
    body = azeventhub.get_body().decode("utf-8")

    try:
        event_dict = json.loads(body)
    except json.JSONDecodeError:
        logging.error(f"REJECTED: invalid JSON -> {body}")
        return

    # Validación de ingreso a bronze
    is_valid, errors = validate_event(event_dict)

    if is_valid:
        logging.info(f"VALID event_id={event_dict.get('event_id')}")

        # Guardar en bronze/validated
        write_event(event_dict, "bronze", "validated")

        # Transformar a silver
        silver_record = transform_to_silver(event_dict)

        # Validar reglas de curación en silver
        silver_is_valid, silver_errors = validate_silver_record(silver_record)

        logging.info(f"SILVER CHECK order_total={silver_record.get('order_total')}")
        logging.info(
            f"SILVER VALIDATION RESULT={silver_is_valid}, errors={silver_errors}"
        )

        if silver_is_valid:
            # Guardar en silver/curated
            write_event(silver_record, "silver", "curated")

            current_order = build_current_order(silver_record)

            existing_current_order = read_existing_current_order(current_order.get("order_id"))

            if should_overwrite_current_order(existing_current_order, current_order):
                write_event(
                    current_order,
                    "silver",
                    "current_orders",
                    file_name=current_order.get("order_id")
                )
                logging.info(
                    f"CURRENT_ORDER UPDATED order_id={current_order.get('order_id')} "
                    f"rank={current_order.get('last_event_sequence_rank')}"
                )
            else:
                logging.info(
                    f"CURRENT_ORDER SKIPPED order_id={current_order.get('order_id')} "
                    f"incoming_rank={current_order.get('last_event_sequence_rank')} "
                    f"existing_rank={existing_current_order.get('last_event_sequence_rank')}"
                )            
        else:
            # Guardar en silver/quarantine
            silver_quarantine_payload = {
                "curation_status": "quarantined",
                "curation_errors": silver_errors,
                "processed_at_utc": datetime.utcnow().isoformat() + "Z",
                "original_silver_record": silver_record
            }

            write_event(silver_quarantine_payload, "silver", "quarantine")

    else:
        logging.warning(
            f"REJECTED event_id={event_dict.get('event_id')} errors={errors}"
        )

        rejected_payload = {
            "validation_status": "rejected",
            "rejection_reason": errors,
            "ingestion_timestamp_utc": datetime.utcnow().isoformat() + "Z",
            "original_event": event_dict
        }

        # Guardar en bronze/rejected
        write_event(rejected_payload, "bronze", "rejected")

@app.route(route="gold-batch", auth_level=func.AuthLevel.FUNCTION)
def gold_batch_function(req: func.HttpRequest) -> func.HttpResponse:
    try:
        result = run_gold_batch_for_today()

        response_body = {
            "status": "success",
            "message": "Gold batch executed successfully.",
            "details": result
        }

        return func.HttpResponse(
            json.dumps(response_body, indent=2),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        response_body = {
            "status": "error",
            "message": str(e),
            "trace": traceback.format_exc()
        }

        return func.HttpResponse(
            json.dumps(response_body, indent=2),
            status_code=500,
            mimetype="application/json"
        )