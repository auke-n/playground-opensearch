# Functional Requirements

## FR-001: Reproducible demo environment

Terraform shall provision a single EC2-hosted demo environment and the minimum supporting AWS resources required to access it safely.

## FR-002: Event ingestion

The demo shall generate realistic operational events and ingest them into OpenSearch through a documented pipeline.

## FR-003: Search and analytics

The demo shall provide examples of full-text search, exact filters, time-range filtering, aggregations, and pagination against the ingested data.

## FR-004: Dashboard visualization

The demo shall provide importable OpenSearch Dashboards objects that visualize service volume, errors, latency, and deployment activity.

## FR-005: Learning walkthrough

The repository shall contain hands-on instructions explaining each major OpenSearch concept through actions that can be performed in the demo.

## FR-006: Operational exercises

The demo shall include documented exercises for cluster/index health, mappings, aliases, rollover or retention, snapshots, and basic troubleshooting.
