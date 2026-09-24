# ADR-0001: Use a single-node EC2 OpenSearch demo topology

## Status

Accepted.

## Context

The project needs a short-lived, low-cost, reproducible environment for learning OpenSearch. The initial focus is product behavior and foundational operations, not production high availability.

## Decision

Provision one ARM-based `t4g.small` EC2 instance with CloudFormation. Run OpenSearch and OpenSearch Dashboards as Docker Compose services on that host. Allocate a 20 GiB encrypted gp3 root volume and a 2 GiB swap file. Bind service ports to loopback only and use AWS Systems Manager Session Manager port forwarding for access.

The OpenSearch Security plugin is disabled only in this first local-access-only learning environment. The required OpenSearch container bootstrap password is supplied as a CloudFormation `NoEcho` parameter and is never committed. Security, TLS, and RBAC will be introduced as a separate hardening exercise.

## Consequences

- A single node is a valid OpenSearch cluster but has no high availability or replica resilience.
- `t4g.small` is the least expensive practical 2 GiB Graviton option, but performance is intentionally constrained and unsuitable for production.
- No inbound security-group rules and no SSH key reduce exposure; the operator needs AWS SSM permissions.
- ARM64 image compatibility is required for every container in the stack.

## Alternatives considered

- `t4g.micro` or `t3.micro`: rejected because 1 GiB memory is too small for OpenSearch and Dashboards.
- Three-node cluster: deferred because it materially increases cost and is not necessary for the first learning stage.
- AWS Managed OpenSearch Service: deferred for a later comparison exercise because it hides host-level operational details.
