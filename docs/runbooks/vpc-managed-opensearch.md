# VPC-First Managed OpenSearch Demo

The `opensearch-vpc.yaml` stack creates all required network resources and a private Amazon OpenSearch Service domain.

## Dashboard access

Retrieve `GeneratorInstanceId` from the CloudFormation outputs, then start a local SSM port-forward:

```powershell
aws ssm start-session --target <generator-instance-id> --document-name AWS-StartPortForwardingSession --parameters portNumber=5601,localPortNumber=5601 --region eu-central-1 --profile borys
```

Open `http://localhost:5601/_dashboards/` and sign in using the credential in the `AdminCredentialsSecretArn` output.

## Verify ingestion

Use SSM to connect to the generator instance:

```bash
sudo systemctl status opensearch-event-generator
sudo journalctl -u opensearch-event-generator -f
```

The bootstrap deploys the index template, ingest pipeline, and saved dashboard objects before beginning continuous event ingestion.

## Cost control

The stack contains a managed OpenSearch domain, a `t3.micro` EC2 instance, and a public IPv4 address. Delete the stack after the learning exercise. It does not create a NAT Gateway.
