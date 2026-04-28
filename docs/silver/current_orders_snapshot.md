# Current Orders Snapshot

## 1. Purpose

The `current_orders` dataset represents the **latest state of each order**.

It converts an event stream into a **deterministic, queryable state**, enabling reliable analytics.

---

## 2. Why a Snapshot is Needed

Event streams describe **what happened**, but not **what is true now**.

Without a snapshot:

* Queries require replaying all events
* Business state is harder to interpret
* Analytics becomes inefficient

The snapshot solves this by maintaining **one record per order** with its current status.

---

## 3. How It Works

Each curated Silver record is transformed into a **current state representation**.

If a record for the same `order_id` already exists, the system decides whether to overwrite it.

### Overwrite Logic

```text id="v5n8ru"
1. Higher event_sequence_rank → overwrite
2. Lower event_sequence_rank → ignore
3. Same rank → compare timestamps (latest wins)
```

This ensures correct ordering even if events arrive out of sequence.

Reference:

* `should_overwrite_current_order()` → 

---

## 4. Event Lifecycle Ordering

Each event type is assigned a sequence rank:

```text id="v61b3w"
order_created       → 1
payment_confirmed   → 2
order_cancelled     → 3
```

This allows the system to resolve:

* Late-arriving events
* Replayed events
* Out-of-order ingestion

---

## 5. Snapshot Structure

Each record represents the **current state of an order**:

```json id="b6rfq3"
{
  "order_id": "string",
  "customer_id": "string",
  "current_status": "CREATED | PAID | CANCELLED",
  "order_total": 100.50,
  "currency_code": "MXN | USD",

  "last_event_type": "string",
  "last_event_timestamp": "ISO8601",
  "last_event_sequence_rank": 1,

  "lifecycle_stage_name": "CREATED_STAGE",
  "status_category": "OPEN | IN_PROGRESS | TERMINAL",

  "is_paid_order": true,
  "is_cancelled_order": false,
  "is_terminal_status": false,

  "business_priority_flag": "HIGH_VALUE | NORMAL",

  "processed_at_utc": "ISO8601",
  "record_type": "current_order_snapshot"
}
```

Reference:

* `build_current_order()` → 

---

## 6. Storage Design

Snapshots are stored in the Silver container:

```text id="ph8y4c"
silver/current_orders/
└── year=YYYY/month=MM/day=DD/
```

Each file represents a single order:

```text id="o3vxr9"
{order_id}.json
```

This enables:

* Fast lookup per entity
* Partitioned storage for scalability

---

## 7. Value Provided

The snapshot layer provides:

* **Current business state per entity**
* Simplified queries (no event replay needed)
* Deterministic results
* Foundation for aggregations (Gold layer)

---

## 8. Summary

The `current_orders` dataset transforms an event-driven pipeline into a **state-aware system**.

It bridges the gap between:

* Event history
* Business reality

Enabling accurate and efficient analytics.
