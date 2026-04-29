from datetime import datetime

def normalize_string(value):
    if value is None:
        return None
    return str(value).strip()

def normalize_upper(value):
    if value is None:
        return None
    return str(value).strip().upper()

def derive_order_value_tier(order_total):
    if order_total is None:
        return None
    if order_total == 0:
        return "ZERO"
    elif order_total < 500:
        return "LOW"
    elif order_total < 2000:
        return "MEDIUM"
    else:
        return "HIGH"

def get_event_sequence_rank(event_type):
    rank_map = {
        "order_created": 1,
        "payment_confirmed": 2,
        "order_cancelled": 3
    }
    return rank_map.get(event_type, 0)

def get_lifecycle_stage_name(event_type):
    stage_map = {
        "order_created": "CREATED_STAGE",
        "payment_confirmed": "PAYMENT_STAGE",
        "order_cancelled": "CANCELLED_STAGE"
    }
    return stage_map.get(event_type, "UNKNOWN_STAGE")

def transform_to_silver(event_dict):
    payload = event_dict.get("payload", {})

    order_id = normalize_upper(payload.get("order_id"))
    customer_id = normalize_upper(payload.get("customer_id"))
    currency_code = normalize_upper(payload.get("currency"))
    order_status = normalize_upper(payload.get("status"))

    order_total_raw = payload.get("order_total")
    order_total = round(float(order_total_raw), 2) if order_total_raw is not None else None

    event_type = normalize_string(event_dict.get("event_type"))
    event_timestamp_utc = normalize_string(event_dict.get("event_time"))
    event_date = event_timestamp_utc[:10] if event_timestamp_utc else None

    silver_record = {
        "order_id": order_id,
        "customer_id": customer_id,
        "order_total": order_total,
        "currency_code": currency_code,
        "order_status": order_status,
        "event_type": event_type,
        "source_system": normalize_string(event_dict.get("source_system")),
        "source_event_id": normalize_string(event_dict.get("event_id")),
        "schema_version": normalize_string(event_dict.get("schema_version")),
        "event_timestamp_utc": event_timestamp_utc,
        "event_date": event_date,
        "processed_at_utc": datetime.utcnow().isoformat() + "Z",
        "processing_layer": "silver",
        "data_quality_status": "validated",
        "pipeline_version": "1.0",
        "order_value_tier": derive_order_value_tier(order_total),
        "is_high_value_order": order_total is not None and order_total >= 2000,
        "event_sequence_rank": get_event_sequence_rank(event_type),
        "lifecycle_stage_name": get_lifecycle_stage_name(event_type)
    }

    return silver_record