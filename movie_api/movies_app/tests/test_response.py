from django.test import TestCase
from django.urls import reverse
from rest_framework.test import RequestsClient


class GetResponseTest(TestCase):
    def test_get_root(self):
        client = RequestsClient()
        response_root = client.get('http://127.0.0.1:8000/')
        self.assertEqual(response_root.status_code, 200)

    def test_get_movies(self):
        url = reverse('movie-list-view')
        response_movies = self.client.get(url, format='json')
        self.assertEqual(response_movies.status_code, 200)

    def test_get_comments(self):
        url = reverse('comment-list-view')
        response_comments = self.client.get(url, format='json')
        self.assertEquals(response_comments.status_code, 200)


class PostResponseTest(TestCase):
    def test_post_movie(self):
        url = reverse('movie-list-view')
        response_movies = self.client.post(url, data={'title': 'Incredible'})
        self.assertEqual(response_movies.status_code, 200)

    def test_post_null_title(self):
        url = reverse('movie-list-view')
        response_null_title = self.client.post(url, data={'title': ''})
        self.assertEqual(response_null_title.status_code, 200)
        self.assertContains(response_null_title, "This field may not be blank")
