<p align="center">
<a href="../README.md">Home</a>
</p>

# Repository Structure

## 1. Purpose

This document describes the organization of the repository and the responsibility of each main folder and file.

The project is structured to separate:

- Azure Functions entry points
- Pipeline layer logic
- Event producer logic
- Technical documentation
- Execution and testing evidence

---

## 2. High-Level Structure

```text
azure-event-driven-data-pipeline/
├── app/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── shared/
├── producer/
├── docs/
│   ├── architecture/
│   ├── ingestion/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── data_flow/
│   ├── design_decisions/
│   └── testing_scenarios/
├── function_app.py
├── host.json
├── requirements.txt
├── local.settings.json
├── .gitignore
└── README.md
```

--- 

## 3. Source Code

`app/` 

Contains the main pipeline logic, organized by responsibility and Medallion layer.

```text 
app/
├── bronze/
│   └── validators.py
├── silver/
│   ├── transformers.py
│   ├── validators.py
│   ├── current_orders.py
│   └── current_order_state.py
├── gold/
│   └── gold_aggregations.py
└── shared/
    └── writers.py
```

| Sub-folder |	Responsibility |
|--------|-----------------|
| `bronze` | Structural validation for raw incoming events |
| `silver` | Cleansing, enrichment, business validation, and snapshot logic | 
| `gold` | Batch aggregation and business metric generation |
|`shared` |	Shared utilities used across layers |

---

## 4. Azure Functions Entry Point

`function_app.py`

This file defines the Azure Functions entry points used by the pipeline.

It includes:

* Event Hub trigger for real-time ingestion → `sales_ingest_function`
* HTTP trigger for Gold batch execution → `gold_batch_function`

The file remains at the repository root because Azure Functions Core Tools expects the function entry point to be available from the root project context.

--- 

### 5. Event Producer

`producer/`

Contains the Python script used to generate and send test events to Azure Event Hub.

```text 
producer/
└── send_sales_events.py
``` 

The producer supports multiple execution modes to simulate:

* Valid orders
* Invalid business records
* Lifecycle transitions
* High-value orders
* Full demo batches

## 6. Documentation

`docs/`

Contains the technical documentation for the project.

```text 
docs/
├── architecture/
├── ingestion/
├── bronze/
├── silver/
├── gold/
├── data_flow/
├── design_decisions/
└── testing_scenarios/
``` 

| Sub-Folder | Description |
|--------|-------------|
| `architecture/`	| Static architecture, component view, and Medallion design |
| `ingestion/` | Event contract and producer behavior | 
| `bronze/` | Bronze layer behavior, contract, and evidence|
| `silver/` | Silver layer behavior, contract, snapshot logic, and evidence | 
| `gold/` | Gold layer behavior, metrics, and evidence |
| `data_flow/` | End-to-end pipeline flow | 
| `design_decisions/` | Architectural choices and trade-offs |
| `testing_scenarios/` | Test scenarios and expected validation outcomes | 

---

## 7. Configuration Files

| File | Purpose |
|------|---------|
| `host.json` | Azure Functions host configuration |
| `requirements.txt` | Python dependencies |
| `local.settings.json` | Example local configuration template |
| `.gitignore` | Defines files and folders excluded from version control | 
| `README.md` | Main entry point and documentation index | 

---

## 8. Files Not Committed

The following files and folders should not be committed to the repository:

| Item | Reason |
|------|--------|
| `.venv/` | Local Python virtual environment |
| `__pycache__/` | Auto-generated Python cache files |
| `local.settings.json` | Contains local secrets and connection strings | 

--- 

## 9. Summary

This repository is organized to keep the pipeline modular, readable, and easy to navigate.

The structure separates:

* Runtime entry points
* Layer-specific processing logic
* Event simulation
* Documentation
* Execution evidence
* Future testing extensions

This organization supports maintainability and makes the project easier to understand from both a technical and portfolio perspective.