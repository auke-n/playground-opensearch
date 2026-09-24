# Access-Log Ingestion Exercise

## Goal

Observe how an ingest pipeline transforms an unstructured web access log into typed fields that can be filtered, aggregated, and visualized.

## Data flow

```text
Raw `message` -> grok -> date -> scripted enrichment -> typed index fields
```

## Assets

- `opensearch/ingest-pipelines/demo-ops-access-pipeline.json`
- `opensearch/index-templates/demo-ops-access.json`
- `opensearch/sample-data/demo-ops-access.ndjson`

## Expected transformation

The pipeline parses `message`, creates `@timestamp`, `client.ip`, HTTP fields, URL path, and response time. It then derives `event.outcome` and `event.duration`.

For example, the source status `500` becomes `event.outcome: failure`; a response time of `912.5` milliseconds becomes an `event.duration` of `912500000` nanoseconds.

## Explore in Dashboards

1. Open **Discover** and create the `demo-ops-access*` data view using `@timestamp` as its time field.
2. Filter on `event.outcome: failure` to find server errors.
3. Add a terms aggregation on `service.name` and a percentile aggregation on `service.response_time_ms`.
4. Compare the original `message` with the fields created by the ingest pipeline.
