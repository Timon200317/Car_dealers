from django.test import TestCase
from django_countries import countries
from rest_framework import status
from rest_framework.utils import json
from djangoTask.src.apps.CarDealer.models import CarDealer
from djangoTask.src.core.enums.enums import UserProfile
from rest_framework.test import APIClient
from djangoTask.src.tests.factories.cars_factory import CarFactory
from djangoTask.src.tests.factories.car_dealer_factory import CarDealerFactory
from djangoTask.src.tests.factories.user_factory import UserFactory


CAR_DEALERS_API_ENDPOINT = "/api/v1/car_dealers/list/"


class CarDealerViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory(user_type=UserProfile.CAR_DEALER)
        self.cars = CarFactory.create_batch(3)
        self.new_car = CarFactory()
        specification = {
            "brand": "BMW",
            "model": "M2 Competition",
            "quantity": 2,
            "max_price": 1000000,
            "color": "WHITE",
        }
        self.car_dealer = CarDealerFactory(
            user=self.user,
            cars=self.cars,
            country=countries[0],
            specification=json.dumps(specification),
        )

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def get_unauthenticated_client(self):
        client = APIClient()
        return client

    def test_get_car_dealers_list_authenticated(self):
        response = self.get_authenticated_client().get(CAR_DEALERS_API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_car_dealers_list_unauthenticated(self):
        response = self.get_unauthenticated_client().get(CAR_DEALERS_API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_balance_field_authenticated(self):
        updated_data = {
            "dealer_name": self.car_dealer.dealer_name,
            "country": self.car_dealer.country,
            "specification": self.car_dealer.specification,
            "balance": 100000,
        }
        response = self.get_authenticated_client().put(
            f"{CAR_DEALERS_API_ENDPOINT}{self.car_dealer.id}/", updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_car_dealer_authenticated(self):
        response = self.get_authenticated_client().delete(f"{CAR_DEALERS_API_ENDPOINT}{self.car_dealer.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.car_dealer.refresh_from_db()
        self.assertEqual(CarDealer.objects.filter(is_active=True).count(), 0)

    def test_delete_car_dealer_unauthenticated(self):
        response = self.get_unauthenticated_client().delete(f"{CAR_DEALERS_API_ENDPOINT}{self.car_dealer.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.car_dealer.refresh_from_db()
        self.assertEqual(CarDealer.objects.filter(is_active=True).count(), 1)



