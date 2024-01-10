from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.tests.factories.user_factory import UserFactory

USERS_API_ENDPOINT = "/api/v1/users/list/"


class UserViewTest(TestCase):
    def setUp(self):
        self.client = UserFactory(user_type=UserProfile.CLIENT)

    def get_authenticated_user(self):
        client = APIClient()
        client.force_authenticate(user=self.client)
        return client

    def get_unauthenticated_user(self):
        client = APIClient()
        return client

    def test_get_user_authenticated(self):
        client = self.get_authenticated_user()
        response = client.get(f"{USERS_API_ENDPOINT}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["username"], self.client.username)
        self.assertEqual(response.data[0]["email"], self.client.email)

    def test_get_list_of_users_without_permission(self):
        client = self.get_unauthenticated_user()
        response = client.get(f"{USERS_API_ENDPOINT}")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
