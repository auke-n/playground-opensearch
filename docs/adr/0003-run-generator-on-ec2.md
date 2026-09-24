# ADR-0003: Run the managed-domain event generator on a dedicated EC2 instance

## Status

Accepted.

## Context

The operational event generator was initially run from a developer workstation. That required local credentials and stopped producing data whenever the local process or computer stopped. Amazon OpenSearch Service does not provide execution access to its managed data nodes.

## Decision

Add a `t3.micro` Amazon Linux 2023 EC2 instance to the managed OpenSearch CloudFormation stack. It installs Python 3.11, runs the generator as a `systemd` service, and has no inbound security-group rules or SSH access.

The instance uses an IAM role with `AmazonSSMManagedInstanceCore` and only `secretsmanager:GetSecretValue` for the domain-admin secret created by this stack. On every service start it retrieves the credential from Secrets Manager, then sends events through the public HTTPS domain endpoint. The bootstrap clones the configured public repository and revision.

## Consequences

- The dashboard receives continuous events independently of a developer workstation.
- The stack gains the cost of a `t3.micro` instance and a public IPv4 address.
- The configured subnet must provide outbound HTTPS access; a private subnet would require NAT or VPC endpoints plus a code-artifact delivery path.
- A public Git repository is an explicit bootstrap dependency. Production deployments should use a pinned immutable artifact from S3 or an approved artifact registry.
