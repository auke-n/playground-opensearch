"""Command-line entry point for continuous or finite operational event ingestion."""

from __future__ import annotations

import argparse
from time import sleep

from .events import AccessEventFactory
from .opensearch import OpenSearchBulkClient, OpenSearchBulkError


def parse_args() -> argparse.Namespace:
    """Parse generator options."""
    parser = argparse.ArgumentParser(description="Generate demo access logs and index them with the Bulk API.")
    parser.add_argument("--endpoint", default="http://localhost:9200", help="OpenSearch endpoint URL.")
    parser.add_argument("--index", default="demo-ops-access-000001", help="Target index name.")
    parser.add_argument("--count", type=int, default=100, help="Number of events to generate; ignored with --continuous.")
    parser.add_argument("--batch-size", type=int, default=25, help="Documents per Bulk API request.")
    parser.add_argument("--interval-seconds", type=float, default=1.0, help="Delay between batches in continuous mode.")
    parser.add_argument("--continuous", action="store_true", help="Generate batches until interrupted with Ctrl+C.")
    parser.add_argument("--seed", type=int, default=None, help="Optional seed for reproducible event sequences.")
    arguments = parser.parse_args()
    if arguments.count < 1 or arguments.batch_size < 1 or arguments.interval_seconds < 0:
        parser.error("count and batch-size must be positive; interval-seconds cannot be negative")
    return arguments


def main() -> None:
    """Generate batches and send them to OpenSearch until complete or interrupted."""
    arguments = parse_args()
    factory = AccessEventFactory(seed=arguments.seed)
    client = OpenSearchBulkClient(endpoint=arguments.endpoint, index=arguments.index)
    indexed_total = 0
    try:
        while arguments.continuous or indexed_total < arguments.count:
            current_batch_size = arguments.batch_size if arguments.continuous else min(arguments.batch_size, arguments.count - indexed_total)
            documents = [factory.create().as_document() for _ in range(current_batch_size)]
            result = client.index_documents(documents)
            indexed_total += result.indexed_count
            print(f"Indexed {result.indexed_count} events in {result.took_ms} ms (total: {indexed_total}).")
            if arguments.continuous:
                sleep(arguments.interval_seconds)
    except KeyboardInterrupt:
        print(f"Stopped after indexing {indexed_total} events.")
    except OpenSearchBulkError as error:
        raise SystemExit(
            f"Ingestion failed: {error}\n"
            f"Verify that OpenSearch is reachable at {arguments.endpoint}. "
            "For the AWS demo, keep the SSM port-forwarding session for port 9200 running."
        ) from error


if __name__ == "__main__":
    main()
