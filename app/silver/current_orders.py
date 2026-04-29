from datetime import datetime

def get_status_category(current_status):
    if current_status in ["CREATED"]:
        return "OPEN"
    elif current_status in ["PAID"]:
        return "IN_PROGRESS"
    elif current_status in ["CANCELLED"]:
        return "TERMINAL"
    else:
        return "UNKNOWN"

def is_terminal_status(current_status):
    return current_status in ["CANCELLED"]

def get_business_priority_flag(order_total):
    if order_total is None:
        return "UNKNOWN"

    if order_total >= 2000:
        return "HIGH_VALUE"
    return "NORMAL"

def build_current_order(silver_record):
    current_status = silver_record.get("order_status")
    order_total = silver_record.get("order_total")

    return {
        "order_id": silver_record.get("order_id"),
        "customer_id": silver_record.get("customer_id"),
        "current_status": current_status,
        "order_total": order_total,
        "currency_code": silver_record.get("currency_code"),
        "last_event_type": silver_record.get("event_type"),
        "last_event_timestamp": silver_record.get("event_timestamp_utc"),
        "last_event_sequence_rank": silver_record.get("event_sequence_rank"),
        "lifecycle_stage_name": silver_record.get("lifecycle_stage_name"),
        "is_terminal_status": is_terminal_status(current_status),
        "status_category": get_status_category(current_status),
        "is_paid_order": current_status == "PAID",
        "is_cancelled_order": current_status == "CANCELLED",
        "business_priority_flag": get_business_priority_flag(order_total),
        "processed_at_utc": datetime.utcnow().isoformat() + "Z",
        "record_type": "current_order_snapshot"
    }