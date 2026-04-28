# Architectural Choices

## 1. Purpose

This document outlines the key architectural decisions made in the pipeline and the rationale behind them.

The goal is to highlight **design intent**, not implementation details.

---

## 2. Medallion Architecture (Bronze → Silver → Gold)

**Decision:**
Use a layered architecture to process data progressively.

**Why:**

* Separates responsibilities across stages
* Enables controlled data quality enforcement
* Preserves raw data while allowing transformations

**Trade-off:**

* Increased storage usage
* More components to manage

---

## 3. Event-Driven Ingestion (Event Hub + Azure Functions)

**Decision:**
Use an event-driven model for ingestion.

**Why:**

* Decouples producers from processing
* Supports real-time data ingestion
* Scales independently between producers and consumers

**Trade-off:**

* Requires handling out-of-order events
* Adds complexity in state management

---

## 4. Hybrid Processing Model (Real-Time + Batch)

**Decision:**
Separate real-time processing (Bronze/Silver) from batch aggregation (Gold).

**Why:**

* Keeps ingestion lightweight and responsive
* Avoids heavy computations in real-time
* Aligns with common data platform patterns

**Trade-off:**

* Metrics are not real-time
* Requires explicit batch execution

---

## 5. Stateful Modeling via Snapshot (current_orders)

**Decision:**
Maintain a snapshot of the latest state per order.

**Why:**

* Event streams alone are not efficient for analytics
* Simplifies queries and downstream processing
* Ensures deterministic results

**Trade-off:**

* Additional storage layer
* Requires overwrite logic and state management

---

## 6. Data Validation Strategy (Multi-Layer)

**Decision:**
Apply validation progressively across layers.

**Why:**

* Bronze ensures structural integrity
* Silver enforces business rules
* Gold relies only on trusted data

**Trade-off:**

* Duplicate validation logic across layers
* Slight increase in processing overhead

---

## 7. Data Lake Storage with Partitioning

**Decision:**
Store data in Azure Data Lake Gen2 using date-based partitioning.

**Why:**

* Improves scalability and performance
* Enables efficient data retrieval
* Aligns with big data storage best practices

**Trade-off:**

* More complex file organization
* Requires consistent partitioning strategy

---

## 8. JSON as Storage Format

**Decision:**
Use JSON across all layers.

**Why:**

* Simplicity and readability
* Easy debugging and inspection
* No dependency on external tooling

**Trade-off:**

* Less efficient than columnar formats (e.g., Parquet)
* Higher storage footprint

**Scope Note:**
Parquet is intentionally excluded from this implementation.

---

## 9. Controlled Event Simulation (Producer)

**Decision:**
Build a custom event producer with predefined scenarios.

**Why:**

* Enables repeatable testing
* Validates pipeline behavior under edge cases
* Supports demonstration and debugging

**Trade-off:**

* Not representative of a real production system
* Requires manual execution

---

## 10. Modular Python Structure

**Decision:**
Organize logic by layer and responsibility.

**Why:**

* Improves maintainability
* Enables independent evolution of components
* Aligns with clean architecture principles

**Trade-off:**

* Slight overhead in project structure
* Requires discipline in code organization

---

## 11. Summary

The architecture prioritizes:

* Data quality
* Traceability
* Scalability
* Separation of concerns

Each decision reflects a trade-off, balancing **simplicity, reliability, and extensibility** in a production-oriented data pipeline.
