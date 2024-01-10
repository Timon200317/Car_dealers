from django.test import TestCase
from rest_framework import status
from djangoTask.src.apps.Car.models import Car
from djangoTask.src.apps.Car.views import CarViewSet
from djangoTask.src.tests.factories.cars_factory import CarFactory
from djangoTask.src.tests.factories.user_factory import UserFactory
from djangoTask.src.core.enums.enums import UserProfile, Color
from rest_framework.test import APIClient

CARS_API_ENDPOINT = "/api/v1/cars/list/"


class CarViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory(user_type=UserProfile.SUPPLIER)
        self.car_1 = CarFactory()

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def get_unauthenticated_client(self):
        client = APIClient()
        return client

    def test_perform_soft_destroy(self):
        view = CarViewSet()
        view.perform_destroy(self.car_1)
        self.car_1.refresh_from_db()
        self.assertFalse(self.car_1.is_active)

    def test_create_new_car_authenticated(self):
        car_data = {
            "brand": "BMW",
            "model": "M2",
            "year": 2023,
            "horse_power_count": 300.00,
            "color": Color.WHITE,
        }
        response = self.get_authenticated_client().post(CARS_API_ENDPOINT, car_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["brand"], car_data["brand"])
        self.assertEqual(response.data["model"], car_data["model"])
        self.assertEqual(response.data["year"], car_data["year"])
        self.assertEqual(response.data["horse_power_count"], car_data["horse_power_count"])
        self.assertEqual(response.data["color"], car_data["color"])

    def test_the_same_new_car_authenticated(self):
        car_data = {
            "brand": self.car_1.brand,
            "model": self.car_1.model,
            "year": self.car_1.year,
            "horse_power_count": self.car_1.horse_power_count,
            "color": self.car_1.color,
        }
        response = self.get_authenticated_client().post(CARS_API_ENDPOINT, car_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_new_car_unauthenticated(self):
        car_data = {
            "brand": "brand",
            "model": "model",
            "year": 2022,
            "horse_power_count": 300,
            "color": Color.WHITE,
        }
        response = self.get_unauthenticated_client().post(CARS_API_ENDPOINT, car_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_car_authenticated(self):
        updated_car_data = {
            "brand": self.car_1.brand,
            "model": "some Model",
            "year": self.car_1.year,
            "horse_power_count": self.car_1.horse_power_count,
            "color": self.car_1.color,
        }
        response = self.get_authenticated_client().put(
            f"{CARS_API_ENDPOINT}{self.car_1.id}/", updated_car_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.car_1.refresh_from_db()
        self.assertEqual(self.car_1.model, "some Model")

    def test_update_car_unauthenticated(self):
        updated_car_data = {
            "brand": self.car_1.brand,
            "model": "some Model",
            "year": self.car_1.year,
            "horse_power_count": self.car_1.horse_power_count,
            "color": self.car_1.color,
        }
        response = self.get_unauthenticated_client().put(
            f"{CARS_API_ENDPOINT}{self.car_1.id}/", updated_car_data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_car_authenticated(self):
        response = self.get_authenticated_client().delete(f"{CARS_API_ENDPOINT}{self.car_1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.filter(is_active=True).count(), 0)

    def test_delete_car_unauthenticated(self):
        response = self.get_unauthenticated_client().delete(f"{CARS_API_ENDPOINT}{self.car_1.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.car_1.refresh_from_db()
        self.assertEqual(Car.objects.filter(is_active=True).count(), 1)
