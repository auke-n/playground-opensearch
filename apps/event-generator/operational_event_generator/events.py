"""Deterministic generation of raw access-log events for the demo."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from random import Random


@dataclass(frozen=True)
class AccessEvent:
    """A raw event accepted by the demo access-log ingest pipeline."""

    message: str
    service_name: str

    def as_document(self) -> dict[str, object]:
        """Return the document shape sent to OpenSearch."""
        return {"message": self.message, "service": {"name": self.service_name}}


class AccessEventFactory:
    """Create realistic, pipeline-compatible access logs from a seeded RNG."""

    _services = {
        "orders-api": ("/api/orders", "/api/orders/42", "/health"),
        "catalog-api": ("/api/catalog", "/api/catalog/42", "/health"),
        "payments-api": ("/api/payments", "/api/payments/42", "/health"),
    }
    _users = ("alice", "bob", "carol", "-")
    _user_agents = ("Mozilla/5.0", "curl/8.7.1", "kube-probe/1.30")
    _client_ips = ("203.0.113.10", "203.0.113.11", "198.51.100.42")

    def __init__(self, seed: int | None = None) -> None:
        self._random = Random(seed)

    def create(self, occurred_at: datetime | None = None) -> AccessEvent:
        """Create one event using UTC time and the demo log format."""
        timestamp = (occurred_at or datetime.now(UTC)).astimezone(UTC)
        service_name = self._random.choice(tuple(self._services))
        path = self._random.choice(self._services[service_name])
        method = "GET" if path == "/health" else self._random.choice(("GET", "GET", "POST"))
        status_code = self._status_code(path)
        response_time_ms = self._response_time_ms(status_code, path)
        body_bytes = self._random.randint(32, 4096)
        referrer = "-" if method == "GET" else "https://demo.example/orders"
        message = (
            f"{self._random.choice(self._client_ips)} - {self._random.choice(self._users)} "
            f"[{timestamp.strftime('%d/%b/%Y:%H:%M:%S %z')}] "
            f'"{method} {path} HTTP/1.1" {status_code} {body_bytes} '
            f'"{referrer}" "{self._random.choice(self._user_agents)}" {response_time_ms:.1f}'
        )
        return AccessEvent(message=message, service_name=service_name)

    def _status_code(self, path: str) -> int:
        if path == "/health":
            return 200
        return self._random.choices((200, 201, 400, 404, 500, 503), (68, 10, 5, 7, 7, 3))[0]

    def _response_time_ms(self, status_code: int, path: str) -> float:
        if path == "/health":
            return self._random.uniform(1, 10)
        if status_code >= 500:
            return self._random.uniform(500, 1500)
        return self._random.uniform(15, 350)
