# Managed Dashboard Exercise

## Dashboard asset

Import `opensearch/dashboards/demo-ops-dashboard.ndjson` into the global tenant to create the `Demo: Operational Event Overview` dashboard.

The dashboard contains four panels:

- Requests over time
- Failed requests
- p95 latency in milliseconds
- HTTP status distribution

## Open the dashboard

Sign in to the managed Dashboards endpoint with the internal admin credentials. Select the **Global** tenant, then navigate to **Dashboards** and open `Demo: Operational Event Overview`.

The dashboard refreshes every 10 seconds and uses a 15-minute time range. Run the Python event generator against the managed endpoint to keep it populated with current events.

## Version control workflow

The NDJSON file is the portable dashboard artifact. Use the Saved Objects export/import workflow to move it between compatible OpenSearch Dashboards environments. It includes the data view and all visualization dependencies.
