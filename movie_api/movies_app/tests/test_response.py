from django.test import TestCase
from rest_framework.test import RequestsClient
from tastypie.test import ResourceTestCaseMixin


class EntryResourceTest(ResourceTestCaseMixin):

    def test_get_api_json(self):
        response = self.api_client.get('/', format='json')
        self.assertValidJSONResponse(response)

    def test_get_movies_json(self):
        response = self.api_client.get('/movies/', format='json')
        self.assertValidJSONResponse(response)

    def test_get_comments_json(self):
        response = self.api_client.get('/comments/', format='json')
        self.assertValidJSONResponse(response)
