# Operational Event Generator

A dependency-free Python CLI that generates raw web access logs and sends them to OpenSearch through the Bulk API. The index default pipeline parses and enriches every document server-side.

## Run

Start an SSM port-forwarding session for port `9200`, then run from this directory:

```powershell
py -3 -m operational_event_generator.cli --count 250 --batch-size 25 --seed 42
```

For a continuous stream, stop with `Ctrl+C`:

```powershell
py -3 -m operational_event_generator.cli --continuous --batch-size 10 --interval-seconds 1
```

## Managed Amazon OpenSearch Service

For a managed domain, set credentials in environment variables and use the HTTPS domain endpoint:

```powershell
$env:OPENSEARCH_USERNAME = 'admin'
$env:OPENSEARCH_PASSWORD = '<retrieved-secret-password>'
py -3 -m operational_event_generator.cli --endpoint https://<domain-endpoint> --continuous
```

## Test

```powershell
py -3 -m unittest discover -s tests -v
```
