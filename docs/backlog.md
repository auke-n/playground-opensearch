# Backlog

## Completed

- [x] ADR-0001: Choose the first deployment topology and security posture.
- [x] Deploy and verify the CloudFormation OpenSearch demo stack.

## Now

- [x] Deploy and verify a managed Amazon OpenSearch Service domain.
- [ ] Define Terraform inputs and AWS network/access boundaries.
- [ ] Scaffold the EC2 bootstrap and containerized OpenSearch stack.
- [x] Define the operational-event schema, index template, and ingest pipeline.
- [~] Implement the Python event generator/API and bulk ingestion.
- [x] Create dashboard objects and import/export workflow.
- [x] Run the managed-domain event generator continuously on a minimal EC2 instance.
- [~] Deploy and verify the self-contained public managed-domain stack with a dedicated generator VPC (ADR-0005).
- [ ] Write the first learning walkthrough and operational runbooks.

## Next

- [ ] Add a minimal React UI only if OpenSearch Dashboards does not cover a learning objective.
- [ ] Add snapshot repository and restore exercise using S3.
- [ ] Add OpenSearch security, TLS, and role-based access control hardening exercise.
- [ ] Compare the EC2 deployment with AWS Managed OpenSearch Service.

## Later

- [ ] Add multi-node cluster, replicas, and failure-recovery exercise.
- [ ] Add CI validation for Terraform, Python, and dashboard assets.
