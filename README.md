# Azure Event-Driven Data Pipeline

## 📌 Overview

This project is a **hands-on exercise** that demonstrates the design and implementation of a data pipeline using Azure services under a **[Medallion Architecture approach](docs/architecture/medallion_design.md) (Bronze → Silver → Gold)**.

Its purpose is to illustrate how core Azure components interact in a real-world scenario, combining **event-driven ingestion, data validation, state modeling, and business aggregation**.

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

## 📚 Structure
| Item | Description | 
|------|-------------|
|🏗️ [Architecture](docs/architecture/overview.md) | How the pipeline is constructed |
|🔄 [Pipeline execution](docs/data_flow/pipeline_execution.md) | How data moves through the pipeline |
| ⚙️ [Design Decisions](docs/design_decisions/design_decisions.md) | Key architectural choices and trade-offs |
| 🧪 [Testing Scenarios](docs/design_testing_scenarios.md) | How pipeline behaves on different execution modes |
| 📁 [Repository Structure](/docs/repository_structure.md) | Project organization |

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
