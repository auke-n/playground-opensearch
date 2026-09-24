from datetime import UTC, datetime
import unittest

from operational_event_generator.events import AccessEventFactory


class AccessEventFactoryTests(unittest.TestCase):
    def test_generated_event_matches_the_ingest_log_shape(self) -> None:
        event = AccessEventFactory(seed=7).create(datetime(2026, 9, 24, 8, 0, tzinfo=UTC))

        self.assertIn("[24/Sep/2026:08:00:00 +0000]", event.message)
        self.assertIn('HTTP/1.1"', event.message)
        self.assertIn("service", event.as_document())


if __name__ == "__main__":
    unittest.main()
