"""Unit tests for the counter service API."""
from unittest import TestCase

from service.common import status
from service.routes import app, reset_counters


class CounterTest(TestCase):
    """REST API server tests."""

    @classmethod
    def setUpClass(cls):
        app.testing = True

    def setUp(self):
        reset_counters()
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_counter(self):
        response = self.client.post("/counters/example")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.get_json(), {"name": "example", "counter": 0})

    def test_duplicate_counter_conflicts(self):
        self.client.post("/counters/example")
        response = self.client.post("/counters/example")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_list_counters(self):
        response = self.client.get("/counters")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get_json(), [])
        self.client.post("/counters/example")
        self.assertEqual(len(self.client.get("/counters").get_json()), 1)

    def test_read_counter(self):
        self.client.post("/counters/example")
        response = self.client.get("/counters/example")
        self.assertEqual(response.get_json(), {"name": "example", "counter": 0})

    def test_increment_counter(self):
        self.client.post("/counters/example")
        response = self.client.put("/counters/example")
        self.assertEqual(response.get_json(), {"name": "example", "counter": 1})

    def test_increment_missing_counter_returns_404(self):
        response = self.client.put("/counters/missing")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_counter(self):
        self.client.post("/counters/example")
        response = self.client.delete("/counters/example")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.client.get("/counters/example").status_code, status.HTTP_404_NOT_FOUND)
