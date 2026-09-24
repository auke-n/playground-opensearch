# Managed EC2 Event Generator

The managed OpenSearch CloudFormation stack provisions an Amazon Linux 2023 `t3.micro` instance that runs the Python event generator continuously through `systemd`.

## Prerequisites

- The selected subnet must be public, or otherwise have outbound HTTPS connectivity.
- `GeneratorRepositoryUrl` must be anonymously cloneable by the EC2 instance.

## Verify the service

Get the instance ID from the `GeneratorInstanceId` CloudFormation output. Start an SSM shell session, then inspect the service:

```bash
sudo systemctl status opensearch-event-generator
sudo journalctl -u opensearch-event-generator -f
```

The service retrieves its credential from Secrets Manager at every startup. It does not write the password to the unit file, environment file, or repository.

## Control the service

```bash
sudo systemctl restart opensearch-event-generator
sudo systemctl stop opensearch-event-generator
sudo systemctl start opensearch-event-generator
```

## Cost control

The `t3.micro` instance and public IPv4 address incur charges while the stack exists. Delete the CloudFormation stack after the learning exercise to remove the instance, domain, secret, and security group.
