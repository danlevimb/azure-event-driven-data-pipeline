# Metrics Definition

## 1. Purpose

This document defines the business metrics generated in the Gold layer.

All metrics are computed from the **current_orders snapshot**, ensuring consistency and reliability.

---

## 2. Aggregation Dimensions

Metrics are grouped by:

* `summary_date` → derived from the last event timestamp
* `currency_code` → ensures separation of monetary values

---

## 3. Metrics

### total_orders

**Definition:**
Total number of orders in the dataset.

**Logic:**
Count of all records.

---

### paid_orders

**Definition:**
Number of orders with status `PAID`.

**Logic:**
Count where `is_paid_order = true`

---

### cancelled_orders

**Definition:**
Number of orders with status `CANCELLED`.

**Logic:**
Count where `is_cancelled_order = true`

---

### high_value_orders

**Definition:**
Number of orders classified as high value.

**Logic:**
Count where `business_priority_flag = HIGH_VALUE`

---

### gross_revenue

**Definition:**
Total value of all orders, regardless of status.

**Logic:**
Sum of `order_total` across all records

---

### net_revenue

**Definition:**
Revenue from completed (paid and not cancelled) orders.

**Logic:**
Sum of `order_total` where:

* `is_paid_order = true`
* `is_cancelled_order != true`

---

### cancelled_revenue

**Definition:**
Total value of cancelled orders.

**Logic:**
Sum of `order_total` where `is_cancelled_order = true`

---

### avg_order_value

**Definition:**
Average value per order.

**Logic:**
`gross_revenue / total_orders`

---

## 4. Data Quality Considerations

* Metrics are computed only from **validated snapshot data**
* Currency is not mixed across aggregations
* Invalid or quarantined records are excluded upstream

---

## 5. Summary

These metrics provide a **consistent and business-aligned view of order activity**.

They are designed to support:

* Operational monitoring
* Revenue analysis
* Business performance tracking
