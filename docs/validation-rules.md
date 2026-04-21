# Validation Rules — Sales Orders Events

## Objective
Ensure that only valid and well-structured events are accepted into the bronze validated layer.

---

## Required Fields

### Envelope
- event_id (string, not null)
- event_type (string, not null)
- schema_version (string, not null)
- source_system (string, not null)
- event_time (datetime, ISO 8601)

### Payload
- payload.order_id (string, not null)
- payload.customer_id (string, not null)
- payload.order_total (number, >= 0)

---

## Allowed Values

### event_type
- order_created
- order_updated
- payment_confirmed
- order_cancelled

---

## Validation Rules

1. The message must be a valid JSON.
2. All required fields must exist and not be null.
3. event_type must be one of the allowed values.
4. event_time must be a valid datetime.
5. payload.order_total must be numeric and >= 0.

---

## Rejection Handling

If any validation fails:
- The event is classified as "rejected"
- The rejection reason must be recorded
- The original message must be preserved for traceability
