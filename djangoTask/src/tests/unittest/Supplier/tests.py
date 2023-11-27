from django.test import TestCase
from django_countries import countries
from rest_framework import status
from rest_framework.test import APIClient

from djangoTask.src.apps.Supplier.models import Supplier
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.tests.factories.cars_factory import CarFactory
from djangoTask.src.tests.factories.supplier_factory import SupplierFactory
from djangoTask.src.tests.factories.user_factory import UserFactory

SUPPLIER_API_ENDPOINT = "/api/v1/suppliers/list/"


class SupplierViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory(user_type=UserProfile.SUPPLIER)
        self.supplier = SupplierFactory(user=self.user, country=countries[0])
        self.car_1 = CarFactory()

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def get_unauthenticated_client(self):
        client = APIClient()
        return client

    def test_get_supplier_list_authenticated(self):
        client = self.get_authenticated_client()
        response = client.get(f"{SUPPLIER_API_ENDPOINT}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_supplier_list_unauthenticated(self):
        client = self.get_unauthenticated_client()

        response = client.get(f"{SUPPLIER_API_ENDPOINT}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_supplier_authenticated(self):
        response = self.get_authenticated_client().delete(f"{SUPPLIER_API_ENDPOINT}{self.supplier.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.supplier.refresh_from_db()
        self.assertEqual(Supplier.objects.filter(is_active=True).count(), 0)

    def test_delete_supplier_unauthenticated(self):
        client = self.get_unauthenticated_client()
        response = client.delete(f"{SUPPLIER_API_ENDPOINT}{self.supplier.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.supplier.refresh_from_db()
        self.assertEqual(Supplier.objects.filter(is_active=True).count(), 1)

    def test_update_supplier_authenticated(self):
        client = self.get_authenticated_client()
        updated_data = {
            "supplier_name": self.supplier.supplier_name,
            "country": countries[3],
            "year_of_origin": 2023,
        }
        response = client.put(f"{SUPPLIER_API_ENDPOINT}{self.supplier.id}/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_supplier_unauthenticated(self):
        client = self.get_unauthenticated_client()
        updated_data = {
            "supplier_name": self.supplier.supplier_name,
            "country": countries[3],
            "year_of_origin": 2023,
        }
        response = client.put(f"{SUPPLIER_API_ENDPOINT}{self.supplier.id}/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
