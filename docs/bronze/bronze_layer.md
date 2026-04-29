<p align="center">
<a href="../../README.md">Home</a>
</p>

# 🥉 Bronze Layer

### 1. Purpose

The Bronze layer is responsible for **raw data ingestion**.

It captures events as they arrive from Event Hub and applies [basic structural validation](data_contract.md), without enforcing business rules.

---

### 2. Why Bronze Exists

This layer ensures that:

* Original data is always preserved
* Invalid data is not lost, only separated
* Downstream layers are protected from malformed events

It acts as the **entry checkpoint of the pipeline**.

---

### 3. Transformation & Enrichment
In Bronze layer there is no transformation made to data, just schema validation.

### 4. Validation Strategy

Validation at this stage is limited to **schema-level checks**:

* Required fields must exist
* Payload structure must be valid
* Data types must be correct
* Basic constraints (e.g., non-negative order_total)

Reference:

* [`\app\bronze\validators.py`](../../app/bronze/validators.py)

No business rules are applied at this stage.

---

### 5. Output Zones

Events are separated into two zones:

* [`validated/`](bronze_validated.jpg) → structurally correct events
* [`rejected/`](bronze_rejected.jpg) → invalid events with error details

Rejected events include:

* Validation errors
* Original payload
* Ingestion timestamp

This allows full traceability and debugging.

---

### 6. Storage Design (Data Lake)

The Bronze layer is stored in **Azure Data Lake Storage Gen2**, using a container-based structure.

```text
└── bronze/
    ├── validated/
    │   └── year=YYYY/
    │       └── month=MM/
    │           └── day=DD/
    └── rejected/
        └── year=YYYY/
            └── month=MM/
                └── day=DD/
```

This structure is generated dynamically at write time.

Reference:

* [`app\shared\writers.py`](../../app/shared/writers.py)

---

### 6. Value Provided

The Bronze layer provides:

* **Data traceability** → original events are always preserved
* **Error isolation** → invalid data does not affect downstream layers
* **Reprocessing capability** → raw data can be replayed if needed
* **Scalability** → partitioned storage enables efficient data handling

---

### 7. Summary

The Bronze layer is the **foundation of the pipeline**.

It guarantees that all incoming data is:

* Captured
* Validated structurally
* Properly categorized

Without applying transformations that could compromise data integrity.
