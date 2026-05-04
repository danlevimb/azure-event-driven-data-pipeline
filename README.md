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

To understand how the pipeline is constructed:

[Pipeline components](docs/architecture/overview.md)

## 🔄 Pipeline execution

To understand how data moves through the pipeline:

[Data Flow](docs/data_flow/pipeline_execution.md)

---


## ⚙️ Design Decisions

Key architectural choices and trade-offs:

[Design decisions](docs/design_decisions/design_decisions.md)

---

## 🧪 Testing Scenarios

Take a look at how pipeline behaves on different execution modes:

👉 [Testing Scenarios](docs/design_testing_scenarios.md)

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
