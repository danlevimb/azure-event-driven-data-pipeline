
<p align="center">
<a href="../../README.md">Home</a>
</p>

#  🔄 Pipeline execution

## 1. Overview

This document describes how to execute the pipeline locally, including:

* Event generation
* Real-time ingestion
* Batch aggregation (Gold layer)

---

## 2. Pre-requisites

These are the resources required to run this pipeline.

  * Python 3.13
  * Azure Functions Core Tools
  * Azure Storage Account (Data Lake Gen2)
  * Event Hub namespace

For full requirement list take a look at [requirements.txt](../../requirements.txt)

--- 

## 3. Environment Setup


### 3.1 Download repository

Identify & place repository on desired destination directory.

| Type | Item | Description |
|------|-----------|-------------|
| Directory | `\app` | Functions layers  |
| File | `\producer\send_sales_events.py`| Event producer |
| File| `\function_app.py` | Function container |

### 3.2 Create virtual environment

```bash
python -m venv .venv 
.\.venv\Scripts\Activate
```

### 3.3 Install dependencies

```bash
pip install -r requirements.txt
```

### 3.4 Configure environment variables

Create a local `local.settings.json` file. This file is excluded by `.gitignore` and must never be committed.

Use placeholders in documentation and keep real values only in the local development environment:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "<local-or-azure-storage-connection>",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "EVENT_HUB_CONNECTION": "<event-hub-consumer-connection>",
    "DATALAKE_CONNECTION": "<storage-connection>",
    "PRODUCER_EVENT_HUB_CONNECTION": "<event-hub-producer-connection>"
  }
}
```

For this MVP, the code uses connection-string authentication.

Use separate least-privilege Event Hub shared access policies where possible:

- producer connection: **Send** permission;
- Azure Function trigger connection: **Listen** permission.

Avoid using `RootManageSharedAccessKey` for routine application access.

For a production implementation, prefer identity-based authentication such as Managed Identity where supported and move any remaining secrets to a managed secret store.

---

## 4. Start the Pipeline (Real-Time Layer)

Run the Azure Function on repository directory:

```bash
func start
```
![Function start](func_start.jpg)


## 5. Generate Events (Producer)

Before running producer, take a look at the desired run-mode:

| Mode | Description | Expected Behavior |
|------|------------|------------------|
| `force_zero` | Generates events with `order_total = 0` | Should pass Bronze validation but fail Silver business rules → routed to `silver/quarantine` |
| `force_bad_currency` | Generates events with unsupported currency codes (e.g., EUR) | Should pass Bronze but fail Silver validation → quarantined |
| `force_bad_status` | Generates events with invalid order statuses | Should be rejected at Silver layer due to invalid lifecycle state |
| `same_order_lifecycle` | Generates multiple events for the same `order_id` simulating lifecycle transitions | Validates snapshot overwrite logic in `current_orders` |
| `portfolio_demo_batch` | Generates a mixed dataset (valid, invalid, lifecycle, high-value) | Exercises full pipeline behavior end-to-end across all layers |

#### Validation Mapping

These modes are designed to validate specific pipeline behaviors:

- Bronze Layer → structural validation (schema, required fields)
- Silver Layer → business validation and enrichment
- Snapshot → state correctness and ordering logic
- Gold Layer → aggregation consistency

This allows targeted testing of each pipeline component.

Set the desired mode in the `TEST_MODE` variable inside the producer script.

![TEST_Mode_configuration](send_sales_events.jpg)

#### Notes
- These modes are intentionally designed to simulate real-world data quality scenarios.
- `force_` parameters generate evidence on corresponding locations and stage (`bronze\rejected` - `silver\quarantine`)
- They allow validation of both structural (Bronze) and business (Silver) rules.
- Use `portfolio_demo_batch` mode for demonstrating full pipeline execution.

Now, run the event producer:

```bash
python producer/send_sales_events.py
```

 
This will:

* Send events to Event Hub
* Trigger real-time processing
* Populate Bronze & Silver layers

[Sample Execution Output](producer_results.md)

Below is an example of events generated using `portfolio_demo_batch`:

- Multiple scenarios are produced:
  - paid_order
  - cancelled_order
  - paid_then_cancelled
  - open_order
  - high_value_paid
  - zero_amount
  - bad_currency
  - bad_status

This demonstrates how different event types flow through the pipeline and trigger distinct validation paths.


---

## 6. Execute Gold Layer (Batch)

### Option 1 — Browser

```text
http://localhost:7071/api/gold-batch
```

![Browser results](../gold/batch_trigger_http.jpg)

---

### Option 2 — PowerShell

```powershell
Invoke-RestMethod -Method POST http://localhost:7071/api/gold-batch
```

![Terminal results](../gold/batch_trigger_terminal.jpg)

## 7. Validate Outputs

Check data in Azure Data Lake Containers:

``` text
Azure Data Lake Storage Gen2
├── bronze/
│   ├── validated/
│   └── rejected/
├── silver/
│   ├── curated/
│   ├── quarantine/
│   └── current_orders/
└── gold/
    └── daily_order_summary/
```

---

## 8. Summary

This execution flow demonstrates a hybrid pipeline using the following steps:

```text
1. Start Azure Function
2. Run producer
3. Validate Bronze & Silver outputs
4. Trigger Gold batch
5. Validate aggregated results
```







