# Data Contract

## 1. Input Event

The Bronze layer receives events with the following structure:

```json
{
  "event_id": "string",
  "event_type": "string",
  "schema_version": "string",
  "source_system": "string",
  "event_time": "ISO8601",
  "payload": {
    "order_id": "string",
    "customer_id": "string",
    "order_total": "number",
    "currency": "string",
    "status": "string"
  }
}
```

---

## 2. Validated Output

If the event passes schema validation, it is stored **unchanged** in:

```text
bronze/validated/
```

No transformations are applied at this stage.

---

## 3. Rejected Output

If validation fails, the event is wrapped with error metadata:

```json
{
  "validation_status": "rejected",
  "rejection_reason": ["list of errors"],
  "ingestion_timestamp_utc": "ISO8601",
  "original_event": { ... }
}
```

Stored in:

```text
bronze/rejected/
```

---

## 4. Contract Rules

* The original event is never modified
* Invalid events are not discarded
* All rejected records retain full traceability
