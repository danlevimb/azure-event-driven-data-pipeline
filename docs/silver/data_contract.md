<p align="center">
<a href="../../README.md">Home</a> |
<a href="silver_layer.md">Back</a>
</p

# Silver - Data Contract

## 1. Input Event

The Silver layer receives **validated events from Bronze**.

These events already comply with the basic schema but may still contain invalid business data.

---

## 2. Curated Output

Valid records are transformed into a structured format:

```json id="m0p3yx"
{
  "order_id": "string",
  "customer_id": "string",
  "order_total": 100.50,
  "currency_code": "MXN | USD",
  "order_status": "CREATED | PAID | CANCELLED",
  "event_type": "string",
  "event_timestamp_utc": "ISO8601",
  "event_date": "YYYY-MM-DD",
  "processed_at_utc": "ISO8601",
  "processing_layer": "silver",
  "data_quality_status": "validated",
  "pipeline_version": "1.0",

  "order_value_tier": "LOW | MEDIUM | HIGH",
  "is_high_value_order": true,
  "event_sequence_rank": 1,
  "lifecycle_stage_name": "CREATED_STAGE"
}
```

Stored in:

```text id="8dp63m"
silver/curated/
```

---

## 3. Quarantine Output

If a record fails business validation, it is stored with error metadata:

```json id="p7bl0c"
{
  "curation_status": "quarantined",
  "curation_errors": ["list of errors"],
  "processed_at_utc": "ISO8601",
  "original_silver_record": { ... }
}
```

Stored in:

```text id="3t63tv"
silver/quarantine/
```

---

## 4. Contract Rules

* All curated records must pass business validation
* Invalid records are not discarded, only quarantined
* All records are enriched before storage
* Field names are standardized and normalized
* Derived attributes must be present in all curated records

---

## 5. Notes

* `order_total` must be greater than 0 for curated data
* Only supported currencies (`MXN`, `USD`) are accepted
* Only valid lifecycle statuses are allowed

Reference:

* `transform_to_silver()` → 
* `validate_silver_record()` → 

---

## 6. Summary

The Silver data contract defines a **clean, validated, and enriched structure**.

It ensures that all downstream layers operate on **consistent and business-ready data**.
