# Evidence Index

**Project:** `azure-event-driven-data-pipeline`  
**Status:** Current public proof map

---

## 1. Purpose

This index maps the project's public claims to execution artifacts that are already versioned in the repository.

The evidence is intentionally distributed alongside the layer documentation so each screenshot remains close to the behavior it proves.

## 2. Producer and runtime evidence

| Claim | Evidence |
|---|---|
| Producer sends controlled test scenarios | [Producer execution output](data_flow/producer_results.md) |
| Azure Functions runtime starts locally | [Function startup screenshot](data_flow/func_start.jpg) |
| Producer test mode is configurable | [Producer configuration screenshot](data_flow/send_sales_events.jpg) |

## 3. Bronze evidence

| Claim | Evidence |
|---|---|
| Structurally valid events are persisted | [Bronze validated](bronze/bronze_validated.jpg) |
| Invalid events are isolated | [Bronze rejected](bronze/bronze_rejected.jpg) |
| Rejection metadata is preserved | [Bronze error metadata](bronze/bronze_error_metadata.jpg) |

## 4. Silver and snapshot evidence

| Claim | Evidence |
|---|---|
| Valid records reach the curated zone | [Silver curated](silver/silver_curated.jpg) |
| Business-rule violations are quarantined | [Silver quarantine](silver/silver_quarantine.jpg) |
| Latest order state is persisted | [Current orders snapshot](silver/silver_current_orders.jpg) |
| Lifecycle events are evaluated across the same order | [Bronze lifecycle evidence](testing_scenarios/bronze_validated_lifecycle.jpg) |
| Cancelled lifecycle resolves to final snapshot state | [Silver cancelled order](testing_scenarios/silver_cancelled_order.jpg) |

## 5. Gold evidence

| Claim | Evidence |
|---|---|
| Gold batch can be triggered over HTTP | [HTTP batch trigger](gold/batch_trigger_http.jpg) |
| Gold batch can be triggered from PowerShell | [Terminal batch trigger](gold/batch_trigger_terminal.jpg) |
| Daily business metrics are produced | [Gold daily summary](gold/gold_daily_order_summary.jpg) |
| Currency-specific aggregate output is validated | [Gold MXN summary](testing_scenarios/gold_daily_order_summary_mxn.jpg) |

## 6. End-to-end testing evidence

| Claim | Evidence |
|---|---|
| Controlled scenarios cover valid and invalid routes | [Testing scenarios](testing_scenarios/testing_scenarios.md) |
| Expected routing across layers is documented visually | [Expected data coverage](testing_scenarios/expected_data_coverage.png) |
| Full flow is documented | [End-to-end flow](data_flow/end_to_end_flow.md) |

## 7. Evidence boundary

The repository proves:

- controlled event generation;
- Event Hub ingestion into Azure Functions;
- Bronze structural validation;
- Silver business validation and quarantine;
- current-order state modeling;
- Gold batch aggregation;
- layer-level execution behavior.

It does **not** claim evidence for:

- Infrastructure as Code;
- CI/CD deployment automation;
- Managed Identity / Key Vault integration;
- private networking;
- production monitoring / alerting;
- enterprise-scale throughput;
- exactly-once guarantees.

## 8. Public-safety rule

Evidence must never expose:

- Event Hub access keys;
- storage account keys;
- connection strings;
- SAS tokens;
- subscription / tenant identifiers;
- personal emails;
- other credentials or account-specific secrets.

Authentication examples should use placeholders only.
