# Bulk Event Generator Exercise

## Goal

Generate a live stream of raw access logs and observe the OpenSearch Bulk API applying the index default ingest pipeline.

## Prerequisites

Open a second SSM port-forwarding terminal for the OpenSearch REST API:

```powershell
aws ssm start-session --target <instance-id> --document-name AWS-StartPortForwardingSession --parameters portNumber=9200,localPortNumber=9200 --region eu-central-1 --profile borys
```

Keep that terminal running. It exposes the remote cluster only at `http://localhost:9200`.

## Run the generator

From `apps/event-generator`, run a finite batch:

```powershell
py -3 -m operational_event_generator.cli --count 250 --batch-size 25 --seed 42
```

Or stream events until interrupted:

```powershell
py -3 -m operational_event_generator.cli --continuous --batch-size 10 --interval-seconds 1
```

## Observe the result

In Dashboards Discover, use the `demo-ops-access*` data view and set the time range to the last 15 minutes. The generator emits current UTC timestamps, so new events should appear immediately. Filter on `event.outcome: failure` and inspect the original `message` alongside the parsed fields.

## What to notice

- One Bulk API request indexes many documents, reducing HTTP overhead.
- The client sends raw text only; the index default pipeline performs parsing centrally.
- Index failures are surfaced per item in the Bulk API response.
- The client retries transient transport failures with exponential backoff.
