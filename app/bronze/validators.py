def validate_event(event_dict):
    errors = []

    # Required fields
    required_fields = [
        "event_id",
        "event_type",
        "schema_version",
        "source_system",
        "event_time",
        "payload"
    ]

    for field in required_fields:
        if field not in event_dict or event_dict[field] is None:
            errors.append(f"Missing field: {field}")

    # Payload validation
    payload = event_dict.get("payload", {})

    if "order_id" not in payload:
        errors.append("Missing payload.order_id")

    if "customer_id" not in payload:
        errors.append("Missing payload.customer_id")

    if "order_total" not in payload:
        errors.append("Missing payload.order_total")
    else:
        try:
            if float(payload["order_total"]) < 0:
                errors.append("order_total must be >= 0 for bronze ingestion")
        except:
            errors.append("order_total must be numeric")

    # Event type validation
    allowed_event_types = [
        "order_created",
        "order_updated",
        "payment_confirmed",
        "order_cancelled"
    ]

    if event_dict.get("event_type") not in allowed_event_types:
        errors.append("Invalid event_type")

    return len(errors) == 0, errors