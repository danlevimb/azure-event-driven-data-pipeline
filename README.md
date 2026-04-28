# Azure Event-Driven Data Pipeline

## 📌 Overview

This project is a **hands-on exercise** that demonstrates the design and implementation of a data pipeline using Azure services under a **[Medallion Architecture approach](docs/architecture/medallion_design.md) (Bronze → Silver → Gold)**.

Its purpose is to illustrate how core Azure components interact in a real-world scenario, combining **event-driven ingestion, data validation, state modeling, and business aggregation**.

---

## 🧭 Project Scope

The pipeline covers:

* Real-time event ingestion via Azure Event Hub
* Processing using Azure Functions (Python)
* Data storage in Azure Data Lake Gen2
* Layered data refinement (Bronze / Silver / Gold)
* Stateful modeling using a snapshot dataset
* Batch aggregation for business metrics

---

## 🏗️ Architecture

For a high-level explanation of the system design:

👉 [Architecture Overview](docs/architecture/overview.md)

| Layer| Description |
|------|-------------|
| 📥 [Ingestion](docs/ingestion/event_contract.md) | Event generation and contract definition|
| 🥉 [Bronze](docs/bronze/bronze_layer.md) | Raw ingestion and structural validation |
| 🥈 [Silver](docs/silver/silver_layer.md) | Data cleansing, enrichment, and business validation |
| 🥇 [Gold](docs/gold/gold_layer.md) | Business-ready aggregations and metrics |

👉 [Bronze Data Contract](docs/bronze/data_contract.md)
👉 [Silver Data Contract](docs/silver/data_contract.md)
👉 [Metrics Definition](docs/gold/metrics_definition.md)

---

## 🔄 End-to-End Flow

To understand how data moves through the pipeline:

👉 [End-to-End Data Flow](docs/data_flow/end_to_end_flow.md)

---


---


## ⚙️ Design Decisions

Key architectural choices and trade-offs:

👉 [Architectural Choices](docs/design_decisions/architectural_choices.md)

---

## 🧪 Operations & Testing

Execution and validation of the pipeline:

👉 [How to Run](docs/operations/how_to_run.md)
👉 [Testing Scenarios](docs/operations/testing_scenarios.md)
👉 [Troubleshooting](docs/operations/troubleshooting.md)

---

## 📁 Repository Structure

For a detailed view of the project organization:

👉 [Repository Structure](repo_structure.txt)

---

## 🎯 Key Concepts Demonstrated

* Event-driven data ingestion
* Progressive data validation
* Medallion Architecture implementation
* Stateful modeling from event streams
* Batch vs real-time processing separation
* Data Lake partitioning strategy

---

## 📌 Notes

* This project uses **JSON as the storage format** across all layers
* The implementation is designed for **learning and demonstration purposes**
* Azure Functions are executed locally due to subscription constraints

---

## 🚀 Summary

This repository demonstrates how to build a **modern data pipeline in Azure**, focusing on:

* Data quality
* Traceability
* Scalable design
* Clear separation of responsibilities

It is intended as a **portfolio project** to showcase practical data engineering skills.
