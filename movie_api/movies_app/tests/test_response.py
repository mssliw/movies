from django.test import TestCase
from rest_framework.test import RequestsClient


class GetResponseTest(TestCase):
    def test_get_root(self):
        client = RequestsClient()
        response_root = client.get('http://127.0.0.1:8000/')
        self.assertEquals(response_root.status_code, 200)
