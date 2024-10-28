from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TestViewTests(APITestCase):

    def setUp(self):
        # This URL will be the endpoint for TestView
        self.url = reverse('test')

    def test_get_request(self):
        """Test the GET method returns a 200 OK and correct message."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Hello, World!'})

    def test_post_request(self):
        """Test the POST method logs data and returns the correct response."""
        data = {'key': 'value'}
        
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Posting hello world!'})

