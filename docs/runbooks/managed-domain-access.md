# Managed Amazon OpenSearch Service Access

## Retrieve the domain details

```powershell
aws cloudformation describe-stacks --stack-name playground-opensearch-managed --profile borys --region eu-central-1 --query 'Stacks[0].Outputs' --output table
```

## Retrieve the internal admin credentials

Use the `AdminCredentialsSecretArn` output. Keep the values out of source control and terminal history where possible.

```powershell
$secret = aws secretsmanager get-secret-value --secret-id <secret-arn> --profile borys --region eu-central-1 --query SecretString --output text | ConvertFrom-Json
$env:OPENSEARCH_USERNAME = $secret.username
$env:OPENSEARCH_PASSWORD = $secret.password
```

Open the `DashboardsUrl` stack output and sign in with these credentials.

## Run the Python generator

Set the domain endpoint from the `DomainEndpoint` stack output and run:

```powershell
cd apps/event-generator
py -3 -m operational_event_generator.cli --endpoint https://<domain-endpoint> --continuous --batch-size 10 --interval-seconds 1
```

## Security scope

The domain endpoint is public so that managed Dashboards can proxy data requests. HTTPS and fine-grained access control remain enabled. Do not share the generated credentials, and delete this short-lived learning environment when it is no longer needed.
