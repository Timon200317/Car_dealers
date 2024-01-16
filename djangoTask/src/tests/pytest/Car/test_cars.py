import json

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from djangoTask.src.apps.Car.models import Car
from djangoTask.src.tests.pytest.conftest import car_data

CARS_API_ENDPOINT = "/api/v1/cars/list/"

payload_cars_1 = {"brand": "BMW", "model": "M2", "year": 2023, "horse_power_count": 300}
payload_cars_2 = {"brand": "Audi", "model": "A4", "year": 2022, "horse_power_count": 250}


@pytest.mark.django_db
def test_perform_soft_destroy(user_supplier):
    client = APIClient()
    client.force_authenticate(user=user_supplier)
    car = Car.objects.create(is_active=True)

    response = client.delete(f"{CARS_API_ENDPOINT}{car.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    car.refresh_from_db()


@pytest.mark.django_db
@pytest.mark.parametrize("car_data", [
    {"brand": "BMW", "model": "M2", "year": 2023, "horse_power_count": 300},
    {"brand": "Audi", "model": "A4", "year": 2022, "horse_power_count": 250},
])
def test_create_new_car_authenticated(authenticated_client, car_data):
    client = authenticated_client

    response = client.post(CARS_API_ENDPOINT, data=car_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["brand"] == car_data["brand"]
    assert response.data["model"] == car_data["model"]
    assert response.data["year"] == car_data["year"]
    assert response.data["horse_power_count"] == car_data["horse_power_count"]


@pytest.mark.django_db
@pytest.mark.parametrize("car_data", [
    payload_cars_1,
    payload_cars_2,
])
def test_create_new_car_unauthenticated(unauthenticated_client, car_data):
    client = unauthenticated_client

    response = client.post(CARS_API_ENDPOINT, data=car_data, format='json')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize("car_data", [
    payload_cars_1,
    payload_cars_2,
])
def test_update_car_authenticated(authenticated_client, car_data):
    client = authenticated_client

    car = Car.objects.create(is_active=True, **car_data)

    updated_car_data = {
        "brand": "BMW",
        "model": "some Model",
        "year": 2023,
        "horse_power_count": 300.00,
    }
    response = client.put(f"{CARS_API_ENDPOINT}{car.id}/", updated_car_data)

    assert response.status_code == status.HTTP_200_OK

    car.refresh_from_db()
    assert car.model == "some Model"


@pytest.mark.django_db
@pytest.mark.parametrize("car_data", [
    payload_cars_1,
    payload_cars_2,
])
def test_update_car_unauthenticated(unauthenticated_client, car_data):
    client = unauthenticated_client

    car = Car.objects.create(is_active=True, **car_data)

    updated_car_data = {
        "brand": "BMW",
        "model": "some Model",
        "year": 2023,
        "horse_power_count": 300.00,
    }
    response = client.put(f"{CARS_API_ENDPOINT}{car.id}/", updated_car_data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize("car_data", [
    payload_cars_1,
    payload_cars_2,
])
def test_delete_car_authenticated(authenticated_client, car_data):
    client = authenticated_client

    car = Car.objects.create(is_active=True, **car_data)

    response = client.delete(f"{CARS_API_ENDPOINT}{car.id}/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Car.objects.filter(is_active=True).count() == 3


@pytest.mark.django_db
@pytest.mark.parametrize("car_data", [
    payload_cars_1,
    payload_cars_2,
])
def test_delete_car_unauthenticated(unauthenticated_client, car_data):
    client = unauthenticated_client

    car = Car.objects.create(is_active=True, **car_data)

    response = client.delete(f"{CARS_API_ENDPOINT}{car.id}/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    car.refresh_from_db()
    assert Car.objects.filter(is_active=True).count() == 4
