# ADR-0005: Use a public managed domain with a dedicated generator VPC

## Status

Accepted.

## Context

The private VPC domain required SSM tunneling, VPN, or a public proxy to open Dashboards from a normal browser. The learning workflow requires a direct managed Dashboards URL.

## Decision

Keep the CloudFormation-owned VPC, public subnet, Internet Gateway, and SSM-only EC2 generator. Remove `VPCOptions` from the Amazon OpenSearch Service domain so its managed Dashboards endpoint is publicly reachable.

Fine-grained access control, generated internal credentials, HTTPS, encryption at rest, and node-to-node encryption remain enabled. The domain is explicitly a short-lived learning environment and not a production topology.

## Consequences

- Dashboards can be opened directly through the AWS-managed URL.
- The OpenSearch data-plane endpoint is internet-reachable and requires careful credential handling.
- The previous private VPC domain is replaced; VPC attachment cannot be changed in place.
