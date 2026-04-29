def validate_silver_record(record):
    errors = []

    allowed_currencies = ["MXN", "USD"]
    allowed_statuses = ["CREATED", "PAID", "CANCELLED"]

    if record.get("currency_code") not in allowed_currencies:
        errors.append("Unsupported currency_code")

    if record.get("order_status") not in allowed_statuses:
        errors.append("Unsupported order_status")

    order_total = record.get("order_total")
    if order_total is None:
        errors.append("Missing order_total")
    else:
        try:
            if float(order_total) <= 0:
                errors.append("order_total must be > 0 for silver curation")
        except:
            errors.append("order_total must be numeric in silver")

    if not record.get("order_id"):
        errors.append("Missing order_id in silver")

    if not record.get("customer_id"):
        errors.append("Missing customer_id in silver")

    return len(errors) == 0, errors