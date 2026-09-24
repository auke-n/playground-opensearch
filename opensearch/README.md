# OpenSearch Assets

This directory contains version-controlled OpenSearch resources for the operational-event analytics demo.

| Location | Purpose |
| --- | --- |
| `index-templates/` | Index settings, mappings, and aliases. |
| `ingest-pipelines/` | Server-side transformations run during indexing. |
| `sample-data/` | Input documents used to demonstrate the pipeline. |

Apply the index template before indexing documents. Index raw access-log events into `demo-ops-access-000001` with the `demo-ops-access-pipeline` pipeline.
