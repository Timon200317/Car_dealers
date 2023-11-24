from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.tests.factories.client_factory import ClientFactory
from djangoTask.src.tests.factories.user_factory import UserFactory

CLIENT_API_ENDPOINT = "/api/v1/clients/list/"


class CustomerViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(user_type=UserProfile.CLIENT)
        self.client = ClientFactory(user=self.user)

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.client)
        return client

    def get_unauthenticated_client(self):
        client = APIClient()
        return client

    def test_get_client(self):
        client = self.get_authenticated_client()
        response = client.get(CLIENT_API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["client_name"], self.client.client_name)
        self.assertEqual(response.data[0]["client_second_name"], self.client.client_second_name)

    def test_get_clients_list_authenticated(self):
        response = self.get_authenticated_client().get(CLIENT_API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_clients_list_unauthenticated(self):
        response = self.get_unauthenticated_client().get(CLIENT_API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

