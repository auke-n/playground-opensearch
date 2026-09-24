"""Minimal OpenSearch Bulk API client implemented with the Python standard library."""

from __future__ import annotations

import json
from dataclasses import dataclass
from time import sleep
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class OpenSearchBulkError(RuntimeError):
    """Raised when OpenSearch rejects an entire bulk request or one of its items."""


@dataclass(frozen=True)
class BulkResult:
    """Summary returned after a successful Bulk API request."""

    indexed_count: int
    took_ms: int


class OpenSearchBulkClient:
    """Send document batches to a single OpenSearch endpoint."""

    def __init__(self, endpoint: str, index: str, retries: int = 3) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._index = index
        self._retries = retries

    def index_documents(self, documents: list[dict[str, object]]) -> BulkResult:
        """Index documents with the configured index default pipeline."""
        if not documents:
            return BulkResult(indexed_count=0, took_ms=0)

        payload = self._bulk_payload(documents)
        response = self._request_with_retries(payload)
        if response.get("errors"):
            failures = [item for item in response["items"] if "error" in item.get("index", {})]
            raise OpenSearchBulkError(f"Bulk request contains {len(failures)} failed items: {failures}")
        return BulkResult(indexed_count=len(documents), took_ms=int(response.get("took", 0)))

    def _bulk_payload(self, documents: list[dict[str, object]]) -> bytes:
        lines: list[str] = []
        for document in documents:
            lines.append(json.dumps({"index": {"_index": self._index}}, separators=(",", ":")))
            lines.append(json.dumps(document, separators=(",", ":")))
        return ("\n".join(lines) + "\n").encode("utf-8")

    def _request_with_retries(self, payload: bytes) -> dict[str, Any]:
        request = Request(
            url=f"{self._endpoint}/_bulk",
            data=payload,
            headers={"Content-Type": "application/x-ndjson"},
            method="POST",
        )
        for attempt in range(self._retries + 1):
            try:
                with urlopen(request, timeout=15) as response:
                    return json.loads(response.read().decode("utf-8"))
            except (HTTPError, URLError, TimeoutError) as error:
                if attempt == self._retries:
                    raise OpenSearchBulkError(f"Bulk request failed after {attempt + 1} attempts: {error}") from error
                sleep(2**attempt)
        raise AssertionError("The retry loop must either return or raise.")
