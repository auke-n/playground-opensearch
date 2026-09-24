# CloudFormation Demo Stack

`opensearch-demo.yaml` provisions a learning-only, single-node OpenSearch cluster on one `t4g.small` EC2 instance in a new VPC.

## What it creates

- One ARM64 EC2 instance with 2 GiB RAM and a 20 GiB encrypted gp3 root volume.
- One VPC, public subnet, internet gateway, and route table for outbound bootstrap traffic.
- An instance security group with no inbound rules.
- An IAM instance role granting Systems Manager access.
- Dockerized OpenSearch and OpenSearch Dashboards, bound to `127.0.0.1` on the instance.

This topology is intentionally constrained and is not suitable for production.

## Deploy

Use a strong value for `OpenSearchInitialAdminPassword`. CloudFormation masks it, but never place the value in source control or terminal history.

```powershell
aws cloudformation deploy `
  --profile borys `
  --region eu-central-1 `
  --stack-name playground-opensearch-demo `
  --template-file infrastructure/cloudformation/opensearch-demo.yaml `
  --capabilities CAPABILITY_IAM `
  --parameter-overrides OpenSearchInitialAdminPassword='<strong-password>'
```

## Access

Obtain the instance ID from stack outputs, then start an SSM tunnel locally:

```powershell
aws ssm start-session `
  --target <instance-id> `
  --document-name AWS-StartPortForwardingSession `
  --parameters '{"portNumber":["5601"],"localPortNumber":["5601"]}' `
  --profile borys `
  --region eu-central-1
```

Open `http://localhost:5601` in a browser. The initial demo disables the OpenSearch Security plugin, but no service port is reachable from the network. See ADR-0001 for scope and consequences.

For the REST API, use the same command with port `9200` and then call `http://localhost:9200/_cluster/health`.

## Teardown

The EC2 instance and EBS volume incur charges while the stack exists. When the exercise is finished, deliberately remove it:

```powershell
aws cloudformation delete-stack --stack-name playground-opensearch-demo --profile borys --region eu-central-1
```
