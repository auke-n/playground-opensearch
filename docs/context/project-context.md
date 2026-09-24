# Project Context

## Goal

Build a small, reproducible, cost-conscious OpenSearch demo on AWS that helps a DevOps engineer learn OpenSearch through observable, realistic data ingestion, search, dashboards, and operations.

## Intended audience

The primary user is a DevOps engineer preparing for an OpenSearch-based project interview and starting without prior OpenSearch experience.

## Constraints

- The first deployment target is a single EC2 instance in AWS.
- Infrastructure must be provisioned with Terraform.
- Application services should use Python; a web UI is optional and should be justified by learning value.
- All source code, configuration comments, and repository documentation are in English.
- User-facing collaboration is in Ukrainian.
- The demo must be safe to destroy and designed to avoid unnecessary AWS cost.

## Learning outcomes

- Explain nodes, clusters, indices, shards, replicas, mappings, analyzers, documents, aliases, and index templates.
- Ingest structured and raw log-like events and observe their transformation.
- Use the Query DSL, full-text search, filters, aggregations, and pagination.
- Build and interpret OpenSearch Dashboards visualizations.
- Perform foundational operations: health checks, index lifecycle management, snapshots, access controls, and troubleshooting.

## Initial scope

The demo domain is operational event analytics: generated web-service logs and deployment events are ingested into OpenSearch and explored through OpenSearch Dashboards and a small application.

## Initial deployment decision

The first environment is a single-node OpenSearch cluster on an ARM-based `t4g.small` EC2 instance. OpenSearch and OpenSearch Dashboards are containerized; operator access uses AWS Systems Manager port forwarding rather than public service ports. See ADR-0001.

## Managed service decision

The self-managed EC2 environment was removed after validating the approach. The next environment is a separate Amazon OpenSearch Service domain, documented in ADR-0002. Both implementation paths remain version-controlled for comparison.

## Open questions

- Which AWS region and allowed administrator IP/CIDR should be used for the EC2 security group?
- Should the first demo expose only OpenSearch Dashboards, or also include a React UI?
- Is access to AWS Managed OpenSearch Service also desired as a later comparison exercise?
