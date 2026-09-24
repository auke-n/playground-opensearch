import json
import unittest

from operational_event_generator.opensearch import OpenSearchBulkClient


class OpenSearchBulkClientTests(unittest.TestCase):
    def test_bulk_payload_uses_an_action_and_source_line_per_document(self) -> None:
        client = OpenSearchBulkClient(endpoint="http://localhost:9200", index="demo-ops-access-000001")

        payload = client._bulk_payload([{"message": "first"}, {"message": "second"}]).decode("utf-8").splitlines()

        self.assertEqual(4, len(payload))
        self.assertEqual("demo-ops-access-000001", json.loads(payload[0])["index"]["_index"])
        self.assertEqual({"message": "first"}, json.loads(payload[1]))
