from django.test import TestCase
from django.urls import reverse
from rest_framework.test import RequestsClient
from ..views import MoviesListView


class GetResponseTest(TestCase):
    def test_get_root(self):
        client = RequestsClient()
        response_root = client.get('http://127.0.0.1:8000/')
        self.assertEqual(response_root.status_code, 200)

    def test_get_movies(self):
        url = reverse('movie-list-view')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_comments(self):
        url = reverse('comment-list-view')
        response_comments = self.client.get(url, format='json')
        self.assertEquals(response_comments.status_code, 200)
