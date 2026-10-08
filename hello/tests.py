from django.test import TestCase


class HelloApiTests(TestCase):
    def test_api_returns_hello_world(self):
        response = self.client.get("/api/hello/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["text"], "hello world")