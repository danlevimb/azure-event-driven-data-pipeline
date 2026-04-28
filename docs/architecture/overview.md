# Architecture
<p align="center">
  <img src="diagram.png" width="900"/>
</p>

This project implements a **production-style event-driven data pipeline** using Azure-native services, following the **Medallion Architecture pattern (Bronze → Silver → Gold)**.

The system is designed to:

* Ingest high-frequency transactional events in real time
* Enforce **data quality at multiple stages**
* Maintain a **stateful representation of business entities**
* Generate **aggregated, analytics-ready datasets**

This architecture reflects real-world data engineering scenarios where **data reliability, traceability, and scalability** are critical.

---

## 2. Architectural Style

The pipeline follows a **hybrid processing model**:

| Processing Type       | Purpose                                     |
| --------------------- | ------------------------------------------- |
| Real-time (Streaming) | Event ingestion, validation, enrichment     |
| Batch (On-demand)     | Aggregation and business metrics generation |

### Key Pattern:

* **Event-driven ingestion** using Azure Event Hub
* **Layered data refinement** using Medallion Architecture
* **Stateful modeling** via entity snapshot (current_orders)
* **Separation of concerns** between ingestion and analytics

---

## 4. Core Components

4.1 Event Producer & Ingestion (Azure Event Hub)
4.1.1 Event Producer
4.1.2 Real-Time Processing (Azure Functions)
4.2 Data Lake Storage (ADLS Gen2)
4.2.1 Bronze Layer (Raw Ingestion)
4.2.2 Silver Layer (Cleansing & Enrichment)
4.2.3 Gold Layer (Aggregations)

---

## 8. Summary

This pipeline demonstrates a **complete, production-oriented data engineering workflow**, including:

* Event-driven ingestion
* Multi-layer data validation
* Stateful entity modeling
* Batch aggregation
* Scalable storage design

It reflects real-world patterns used in modern data platforms and serves as a foundation for advanced extensions such as:

* Orchestration (ADF / Airflow)
* Data warehousing
* Streaming analytics
