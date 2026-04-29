import json
import os
import uuid
from collections import defaultdict
from datetime import datetime

from azure.storage.filedatalake import DataLakeServiceClient

def load_local_settings():
    try:
        with open("local.settings.json") as f:
            settings = json.load(f)
            values = settings.get("Values", {})
            for key, value in values.items():
                os.environ[key] = value
    except Exception as e:
        print(f"Warning loading local.settings.json: {e}")

load_local_settings()

DATALAKE_CONNECTION = os.getenv("DATALAKE_CONNECTION")

SILVER_FILE_SYSTEM = "silver"
GOLD_FILE_SYSTEM = "gold"


def get_service_client():
    if not DATALAKE_CONNECTION:
        raise ValueError("Missing DATALAKE_CONNECTION environment variable.")
    return DataLakeServiceClient.from_connection_string(DATALAKE_CONNECTION)


def list_current_order_paths_for_today():
    service_client = get_service_client()
    file_system_client = service_client.get_file_system_client(SILVER_FILE_SYSTEM)

    now = datetime.utcnow()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    target_path = f"current_orders/year={year}/month={month}/day={day}"

    paths = file_system_client.get_paths(path=target_path)

    file_paths = []
    for path in paths:
        if not path.is_directory:
            file_paths.append(path.name)

    return file_paths


def read_json_file(file_system_name, file_path):
    service_client = get_service_client()
    file_system_client = service_client.get_file_system_client(file_system_name)
    file_client = file_system_client.get_file_client(file_path)

    download = file_client.download_file()
    content = download.readall().decode("utf-8")

    return json.loads(content)


def load_current_orders_for_today():
    file_paths = list_current_order_paths_for_today()
    records = []

    for file_path in file_paths:
        try:
            record = read_json_file(SILVER_FILE_SYSTEM, file_path)
            records.append(record)
        except Exception as e:
            print(f"Skipping file due to read/parse error: {file_path} | error={e}")

    return records


def build_daily_order_summary(records):
    grouped = defaultdict(list)

    for record in records:
        summary_date = (record.get("last_event_timestamp") or "")[:10]
        currency_code = record.get("currency_code") or "UNK"

        if not summary_date:
            continue

        key = (summary_date, currency_code)
        grouped[key].append(record)

    summaries = []

    for (summary_date, currency_code), items in grouped.items():
        total_orders = len(items)
        paid_orders = sum(1 for x in items if x.get("is_paid_order") is True)
        cancelled_orders = sum(1 for x in items if x.get("is_cancelled_order") is True)
        high_value_orders = sum(
            1 for x in items if x.get("business_priority_flag") == "HIGH_VALUE"
        )

        gross_order_value = round(
            sum(float(x.get("order_total", 0) or 0) for x in items),
            2
        )

        net_revenue = round(
            sum(
                float(x.get("order_total", 0) or 0)
                for x in items
                if x.get("is_paid_order") is True
                and x.get("is_cancelled_order") is not True
            ),
            2
        )

        cancelled_order_value = round(
            sum(
                float(x.get("order_total", 0) or 0)
                for x in items
                if x.get("is_cancelled_order") is True
            ),
            2
        )

        avg_order_value = round(gross_order_value / total_orders, 2) if total_orders > 0 else 0

        summary = {
            "summary_date": summary_date,
            "currency_code": currency_code,
            "total_orders": total_orders,
            "paid_orders": paid_orders,
            "cancelled_orders": cancelled_orders,
            "high_value_orders": high_value_orders,
            "gross_revenue": gross_order_value,
            "net_revenue": net_revenue,
            "cancelled_revenue": cancelled_order_value,
            "avg_order_value": avg_order_value,
            "processing_layer": "gold",
            "pipeline_version": "1.1",
            "processed_at_utc": datetime.utcnow().isoformat() + "Z",
            "data_quality_status": "VALIDATED"
        }

        summaries.append(summary)

    return summaries


def write_json_file(file_system_name, file_path, data_dict):
    service_client = get_service_client()
    file_system_client = service_client.get_file_system_client(file_system_name)
    file_client = file_system_client.get_file_client(file_path)

    data = json.dumps(data_dict, indent=2)
    data_bytes = data.encode("utf-8")

    file_client.create_file()
    file_client.append_data(data=data_bytes, offset=0, length=len(data_bytes))
    file_client.flush_data(len(data_bytes))


def build_gold_output_path(summary_date, currency_code):
    date_obj = datetime.strptime(summary_date, "%Y-%m-%d")
    year = date_obj.strftime("%Y")
    month = date_obj.strftime("%m")
    day = date_obj.strftime("%d")

    file_name = f"{currency_code}_{uuid.uuid4()}.json"
    return f"daily_order_summary/year={year}/month={month}/day={day}/{file_name}"


def write_daily_summaries_to_gold(summaries):
    for summary in summaries:
        summary_date = summary.get("summary_date")
        currency_code = summary.get("currency_code", "UNK")

        if not summary_date:
            continue

        output_path = build_gold_output_path(summary_date, currency_code)
        write_json_file(GOLD_FILE_SYSTEM, output_path, summary)


def run_gold_batch_for_today():
    records = load_current_orders_for_today()

    if not records:
        return {
            "message": "No current_orders records found for today.",
            "records_loaded": 0,
            "summaries_written": 0
        }

    summaries = build_daily_order_summary(records)

    if not summaries:
        return {
            "message": "No summaries generated.",
            "records_loaded": len(records),
            "summaries_written": 0
        }

    write_daily_summaries_to_gold(summaries)

    return {
        "message": "Gold batch completed successfully.",
        "records_loaded": len(records),
        "summaries_written": len(summaries)
    }

if __name__ == "__main__":
    run_gold_batch_for_today()