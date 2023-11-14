from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.core.factories.user_factory import UserFactory

CLIENTS_API_ENDPOINT = "/api/clients/"


class ClientViewTest(TestCase):
    def setUp(self):
        self.client = UserFactory(user_type=UserProfile.CLIENT)

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.client)
        return client

    def get_unauthenticated_client(self):
        client = APIClient()
        return client

    def test_get_list_of_clients_without_permission(self):
        response = self.get_unauthenticated_client().get(f"{CLIENTS_API_ENDPOINT}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
