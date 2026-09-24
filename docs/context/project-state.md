# Project State

## Current phase

Managed service deployment.

## Completed

- Defined repository working conventions in `AGENTS.md`.
- Established the initial problem statement, learning goals, constraints, and proposed demo domain.
- Selected and documented the initial single-node EC2 topology in ADR-0001.
- Added a CloudFormation template for the OpenSearch demo environment.
- Deployed `playground-opensearch-demo` in `eu-central-1` using the `borys` profile.
- Verified a green, single-node OpenSearch cluster and an HTTP 200 response from OpenSearch Dashboards through SSM.
- Added and deployed the `demo-ops-access` index template and `demo-ops-access-pipeline` ingest pipeline.
- Indexed and verified four transformed operational access-log events in `demo-ops-access-000001`.
- Implemented and unit-tested a dependency-free Python Bulk API event generator for live ingestion through an SSM tunnel.
- Recorded the managed Amazon OpenSearch Service topology in ADR-0002 after the self-managed AWS stack was removed.

## Next decision

Deploy and verify the managed Amazon OpenSearch Service domain, then adapt the generator for authenticated HTTPS ingestion.
