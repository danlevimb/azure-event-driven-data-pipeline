# Known Limitations and Future Improvements

**Project:** `azure-event-driven-data-pipeline`  
**Status:** Completed MVP reference

---

## 1. Purpose

This document defines the intentional boundaries of the foundation project and separates implemented behavior from future production-oriented improvements.

## 2. Current MVP limitations

### JSON across all layers

The implementation intentionally uses JSON in Bronze, Silver, snapshot, and Gold.

This improves readability and debugging but is less efficient than Parquet or Delta for analytical workloads.

### Connection-string authentication

The local MVP reads Event Hub and storage connection values from environment variables / `local.settings.json`.

Secrets are excluded from Git, but connection-string authentication is not the preferred production identity model.

### No Infrastructure as Code

Azure resources were not provisioned through Bicep or Terraform in this project.

### No CI/CD deployment

The repository does not automate Function App or infrastructure deployment.

### No production monitoring / alerting

Logging exists at application/runtime level, but the project does not implement a production observability stack.

### No schema registry

The event contract is documented in the repository rather than enforced through a schema registry.

### Delivery semantics

The MVP does not claim exactly-once processing or enterprise-grade deduplication.

### Small controlled workload

The producer is intentionally synthetic and designed for repeatable behavior testing, not performance benchmarking.

## 3. Future improvements

High-value future improvements would include:

- Managed Identity where supported;
- Azure Key Vault for secrets that cannot be removed;
- separate least-privilege Event Hub policies for producer and consumer;
- Parquet or Delta for downstream analytical layers;
- idempotency / duplicate-event handling;
- schema registry or stronger contract enforcement;
- Infrastructure as Code;
- CI/CD deployment;
- Azure Monitor / Application Insights operational monitoring;
- retry / poison-event strategy;
- automated integration tests;
- lifecycle-aware retention and cleanup.

## 4. Portfolio context

Several of these gaps are intentionally addressed by later projects in the portfolio:

- ADF framework → reusable orchestration and incremental ingestion;
- Databricks → Delta Lake and analytical storage;
- Production-Ready pipeline → IaC, security, observability, alerting;
- Real-Time pipeline → stronger real-time quality and reconciliation;
- Governance POC → classification, stewardship, lineage, and metadata.

The foundation repo should therefore remain historically accurate rather than retrofitting every later capability into it.
