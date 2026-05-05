<p align="center">
  <img src="pipeline_banner.png" width="900"/>
</p>

# Azure Event-Driven Data Pipeline

## 📌 Overview

This project is a **hands-on exercise** that demonstrates the design and implementation of a data pipeline using Azure services under a **[Medallion Architecture approach](docs/architecture/medallion_design.md) (Bronze → Silver → Gold)**.

Its purpose is to illustrate how core Azure components interact in a real-world scenario, combining **event-driven ingestion, data validation, state modeling, and business aggregation**.

> This implementation intentionally uses JSON across all layers for readability, inspection, and demonstration purposes.

---

## 🧭 Scope

The pipeline covers:

* Real-time event ingestion via Azure Event Hub
* Processing using Azure Functions (Python)
* Data storage in Azure Data Lake Gen2
* Layered data refinement (Bronze / Silver / Gold)
* Stateful modeling using a snapshot dataset
* Batch aggregation for business metrics

---

## 📚 Documentation Index

| Item | Description |
|------|-------------|
| 🏗️ [Architecture](docs/architecture/overview.md) | Static view of the pipeline components and their responsibilities |
| 🧱 [Medallion Design](docs/architecture/medallion_design.md) | Rationale behind the Bronze, Silver, and Gold layer separation |
| 📥 [Event Contract & Producer](docs/ingestion/event_contract.md) | Input event structure and producer behavior |
| 🥉 [Bronze Layer](docs/bronze/bronze_layer.md) | Raw ingestion and structural validation |
| 🥈 [Silver Layer](docs/silver/silver_layer.md) | Cleansing, enrichment, business validation, and snapshot preparation |
| 🔁 [Current Orders Snapshot](docs/silver/current_orders_snapshot.md) | Stateful representation of the latest order state |
| 🥇 [Gold Layer](docs/gold/gold_layer.md) | Business-ready aggregation layer |
| 📊 [Metrics Definition](docs/gold/metrics_definition.md) | Definition of Gold business metrics and metadata fields |
| 🔄 [Pipeline Execution](docs/data_flow/pipeline_execution.md) | How to run the pipeline locally and trigger each stage |
| 🧪 [Testing Scenarios](docs/testing_scenarios/testing_scenarios.md) | Expected behavior across different producer execution modes |
| ⚙️ [Design Decisions](docs/design_decisions/design_decisions.md) | Key architectural choices and trade-offs |
| 📁 [Repository Structure](docs/repository_structure.md) | Project organization and folder responsibilities |

---

## 🎯 Key Concepts Demonstrated

* Event-driven data ingestion
* Progressive data validation
* Medallion Architecture implementation
* Stateful modeling from event streams
* Batch vs real-time processing separation
* Data Lake partitioning strategy

---

## 🚀 Summary

This repository demonstrates how to build a **modern data pipeline in Azure**, focusing on:

* Data quality
* Traceability
* Scalable design
* Clear separation of responsibilities

It is intended as a **portfolio project** to showcase practical data engineering skills.

---

## ✒️ Author 
Me 🙃