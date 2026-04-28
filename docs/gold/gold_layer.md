# Gold Layer

## 1. Purpose

The Gold layer is responsible for generating **business-ready datasets**.

It transforms curated data into **aggregated metrics** that can be directly consumed for reporting and analytics.

---

## 2. Why Gold Exists

Even clean data is not enough for analytics.

This layer ensures that:

* Metrics are precomputed
* Data is optimized for consumption
* Business logic is consistently applied

---

## 3. Processing Model

Unlike previous layers, Gold operates as a **batch process**.

It is executed on demand via an HTTP-triggered function:

* `gold_batch_function` → 

This separates:

* Real-time ingestion (Bronze/Silver)
* Analytical processing (Gold)

---

## 4. Data Source

Gold does not consume raw or intermediate events.

It reads from:

```text id="f7r3km"
silver/current_orders/
```

This ensures that all aggregations are based on **validated and state-consistent data**.

---

## 5. Aggregation Logic

Data is grouped by:

* `summary_date`
* `currency_code`

Key metrics generated:

* `total_orders`
* `paid_orders`
* `cancelled_orders`
* `high_value_orders`
* `gross_revenue`
* `net_revenue`
* `cancelled_revenue`
* `avg_order_value`

Reference:

* `run_gold_batch_for_today()` → 

---

## 6. Output Structure

Each aggregation result follows this structure:

```json id="qz1b2k"
{
  "summary_date": "YYYY-MM-DD",
  "currency_code": "MXN | USD",
  "total_orders": 100,
  "paid_orders": 80,
  "cancelled_orders": 20,
  "high_value_orders": 10,
  "gross_revenue": 50000.00,
  "net_revenue": 42000.00,
  "cancelled_revenue": 8000.00,
  "avg_order_value": 500.00,

  "processing_layer": "gold",
  "pipeline_version": "1.1",
  "processed_at_utc": "ISO8601",
  "data_quality_status": "VALIDATED"
}
```

---

## 7. Storage Design (Data Lake)

Gold data is stored in Azure Data Lake Gen2:

```text id="q2t7mc"
gold/daily_order_summary/
└── year=YYYY/month=MM/day=DD/
```

Each file represents a summary for a given date and currency.

This structure supports:

* Efficient querying
* Scalable storage
* Partition pruning

---

## 8. Value Provided

The Gold layer provides:

* Ready-to-use business metrics
* Consistent aggregation logic
* Optimized datasets for reporting
* A stable interface for consumers

---

## 9. Summary

The Gold layer transforms curated data into **actionable insights**.

It is the final step where data becomes:

* Measurable
* Comparable
* Ready for decision-making
