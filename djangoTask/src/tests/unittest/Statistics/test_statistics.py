from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.tests.factories.car_dealer_factory import CarDealerFactory, CarDealerSalesHistoryFactory
from djangoTask.src.tests.factories.cars_factory import CarFactory
from djangoTask.src.tests.factories.client_factory import ClientFactory
from djangoTask.src.tests.factories.supplier_factory import SupplierFactory, SupplierSalesHistoryFactory
from djangoTask.src.tests.factories.user_factory import UserFactory
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

CAR_DEALERS_API_ENDPOINT = "/api/v1/car_dealers/list"
CLIENT_API_ENDPOINT = "/api/v1/clients/list"


class CardDealerStatisticTestCase(APITestCase):
    def setUp(self):
        self.car = CarFactory()
        client_user = UserFactory(user_type=UserProfile.CLIENT)
        self.client = ClientFactory(user=client_user)
        self.user = UserFactory(user_type=UserProfile.CAR_DEALER)
        self.car_dealer = CarDealerFactory(user=self.user)
        supplier_user = UserFactory(user_type=UserProfile.SUPPLIER)
        self.supplier = SupplierFactory(user=supplier_user)

        self.history1 = CarDealerSalesHistoryFactory(
            car=self.car, car_dealer=self.car_dealer, client=self.client
        )
        self.history2 = CarDealerSalesHistoryFactory(
            car=self.car, car_dealer=self.car_dealer, client=self.client
        )

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def test_get_number_of_sells(self):
        client = self.get_authenticated_client()
        response = client.get(
            f"{CAR_DEALERS_API_ENDPOINT}/{self.car_dealer.id}/number-of-sell/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["number_of_sells"],
            self.history1.count + self.history2.count,
        )

    def test_get_showroom_profit(self):
        client = self.get_authenticated_client()
        response = client.get(f"{CAR_DEALERS_API_ENDPOINT}/{self.car_dealer.id}/profit/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profit_sum = (
            self.history1.count * self.history1.price
            + self.history2.count * self.history2.price
        )
        self.assertEqual(
            response.data["profit"],
            profit_sum,
        )

    def test_get_unique_customers(self):
        client = self.get_authenticated_client()
        response = client.get(
            f"{CAR_DEALERS_API_ENDPOINT}/{self.car_dealer.id}/unique-clients/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            len(response.data["unique_clients"]),
            1,
        )


class CustomerStatisticTestCase(APITestCase):
    def setUp(self):
        self.car = CarFactory()
        self.user = UserFactory(user_type=UserProfile.CLIENT)
        self.client = ClientFactory(user=self.user)
        car_dealer_user = UserFactory(user_type=UserProfile.CAR_DEALER)
        self.car_dealer = CarDealerFactory(user=car_dealer_user)

        self.history1 = CarDealerSalesHistoryFactory(
            car=self.car, car_dealer=self.car_dealer, client=self.client
        )

    def get_authenticated_client(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        return client

    def test_get_amount_money_spent(self):
        client = self.get_authenticated_client()
        response = client.get(f"{CLIENT_API_ENDPOINT}/{self.client.id}/total-amount-spent/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            len(response.data["total_client_spent"]),
            1,
        )
        max_spent_sum = self.history1.count * self.history1.price

        self.assertEqual(response.data["total_client_spent"][0], max_spent_sum)
