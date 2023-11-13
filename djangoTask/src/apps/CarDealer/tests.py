from django.test import TestCase
from rest_framework import status
from rest_framework.utils import json

from djangoTask.src.apps.Car.models import Car
from djangoTask.src.core.enums.enums import UserProfile
from rest_framework.test import APIClient
from djangoTask.src.core.factories.cars_factory import CarFactory
from djangoTask.src.core.factories.car_dealer_factory import CarDealerFactory
from djangoTask.src.core.factories.user_factory import UserFactory

# class BaseViewSetTest(TestCase):
#     def test_perform_destroy(self):
#         obj = Car.objects.create()
#         view = BaseViewSet()
#         view.perform_destroy(obj)
#         obj.refresh_from_db()  # Update obj from db
#         self.assertFalse(obj.is_active)
CARS_API_ENDPOINT = "/api/car_dealers/"


class CarDealerViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory(user_type=UserProfile.CAR_DEALER)
        self.cars = CarFactory.create_batch(5)
        self.new_car = CarFactory()
        car_specifications = {
            "brand": "BMW",
            "model": "M2 Competition",
            "quantity": 2,
            "max_price": 100000,
            "color": "WHITE",
        }
        self.showroom = CarDealerFactory(
            cars=self.cars,
            car_specifications=json.dumps(car_specifications),
        )

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def get_unauthenticated_client(self):
        client = APIClient()
        return client

    def test_get_car_dealers_list_authenticated(self):
        response = self.get_authenticated_client().get(CARS_API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_car_dealers_list_unauthenticated(self):
        response = self.get_unauthenticated_client().get(CARS_API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



