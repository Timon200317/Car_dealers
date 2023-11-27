import pytest
from rest_framework.test import APIClient
from djangoTask.src.apps.Car.models import Car

CARS_API_ENDPOINT = "/api/v1/cars/list/"


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def car_data():
    return {
        'brand': 'Toyota',
        'model': 'Camry',
        'horse_power_count': 200,
        'year': 2022,
        'color': 'WHITE',
    }


@pytest.mark.django_db
def test_get_car_list(api_client, car_data):
    Car.objects.create(**car_data)
    response = api_client.get(CARS_API_ENDPOINT)
    assert response.status_code == 200
    assert len(response.json()) == 4
    assert response.json()[3]['brand'] == 'Toyota'
    assert response.json()[3]['model'] == 'Camry'
    assert response.json()[3]['horse_power_count'] == 200
    assert response.json()[3]['year'] == 2022
