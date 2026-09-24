# ADR-0002: Add a managed Amazon OpenSearch Service deployment

## Status

Accepted.

## Context

The initial EC2 deployment was intentionally self-managed to expose host and container operations. The learning objective also requires hands-on experience with Amazon OpenSearch Service, where AWS manages OpenSearch nodes, storage orchestration, service updates, and managed Dashboards.

## Decision

Add a separate CloudFormation template that creates a single-node Amazon OpenSearch Service domain using `t3.small.search` and 10 GiB gp3 storage. It uses HTTPS, encryption at rest, node-to-node encryption, fine-grained access control, and a generated internal admin credential stored in Secrets Manager.

The public domain policy is restricted to a caller-provided IPv4 CIDR. The service is deliberately public for this short-lived learning environment because no bastion or VPN remains after removal of the EC2 stack.

## Consequences

- The managed demo is independent of the removed EC2 resources.
- AWS manages the OpenSearch runtime, but the domain incurs a higher hourly cost than a stopped EC2 instance.
- A public client IP change requires a CloudFormation update to `AllowedClientCidr`.
- The Python generator must use HTTPS and basic authentication when targeting the managed domain.

## Alternatives considered

- Reusing the EC2 deployment: rejected because it is self-managed, not Amazon OpenSearch Service.
- VPC-only domain: deferred because it requires a new private connectivity path such as a bastion, VPN, or Client VPN.
- IAM master user without Cognito or SAML: rejected because Dashboards sign-in is not functional in that configuration.
