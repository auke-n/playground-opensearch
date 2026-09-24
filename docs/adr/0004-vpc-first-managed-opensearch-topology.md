# ADR-0004: Replace the public managed domain with a self-contained VPC-first topology

## Status

Superseded by ADR-0005.

## Context

The initial managed-domain stack depended on an account default VPC and exposed the OpenSearch endpoint publicly. It was useful for fast learning, but it did not create the network boundary itself and was not a self-contained infrastructure implementation.

## Decision

Create a replacement CloudFormation stack that owns a VPC, Internet Gateway, route table, public generator subnet, private OpenSearch subnet, security groups, managed domain, and generator EC2 instance.

The domain has a VPC endpoint in the private subnet. The generator uses a public subnet only for outbound HTTPS to GitHub, AWS APIs, and SSM; its security group has no inbound rules. There is no NAT Gateway to avoid its fixed hourly and data-processing cost. Nginx on the generator proxies managed Dashboards to an SSM local port-forward, so the private dashboard remains usable without public inbound access.

## Consequences

- The new topology is reproducible without an account default VPC.
- The existing public domain cannot be moved into a VPC in place; it must be deleted and replaced.
- The generated events, index template, ingest pipeline, and version-controlled dashboard assets are initialized on the new domain during EC2 bootstrap.
- Users access Dashboards through SSM at `http://localhost:5601`, not through a public AWS endpoint.
- The public EC2 IPv4 address incurs a small hourly charge. The demo intentionally avoids NAT Gateway charges.
