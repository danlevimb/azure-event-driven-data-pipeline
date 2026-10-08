# Cost Controls

**Project:** `azure-event-driven-data-pipeline`

## Cost posture

This foundation project was designed as a small Azure MVP rather than a continuously running production platform.

Cost-aware choices include:

- small controlled event batches;
- lightweight Azure Functions processing;
- Event Hubs used only for the project workload;
- ADLS Gen2 for low-cost object storage;
- Gold aggregation triggered on demand rather than continuously;
- no Dedicated SQL, Spark, Databricks, or always-on analytical compute.

## Operational cleanup

After validation, unused Azure resources should be stopped or deleted according to whether the project is still being demonstrated.

Relevant resources include:

- Event Hubs namespace / event hub;
- Azure Function App resources;
- Storage Account / ADLS Gen2 data;
- supporting Resource Group resources.

## Important boundary

This repository documents a cost-aware architecture but does not claim a formal cost benchmark or production FinOps model.
