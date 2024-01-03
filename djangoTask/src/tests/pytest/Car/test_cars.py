import pytest
from rest_framework import status
from rest_framework.test import APIClient
from djangoTask.src.apps.Car.models import Car
from djangoTask.src.tests.pytest.conftest import car_data

CARS_API_ENDPOINT = "/api/v1/cars/list/"


@pytest.mark.django_db
def test_perform_soft_destroy(user):
    client = APIClient()
    client.force_authenticate(user=user)
    car = Car.objects.create()

    response = client.delete(f"{CARS_API_ENDPOINT}{car.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    car.refresh_from_db()
    assert not car.is_active


@pytest.mark.django_db
@pytest.mark.parametrize("authenticated", [True, False])
def test_create_new_car(authenticated, user_supplier, authenticated_client, unauthenticated_client):
    client = authenticated_client if authenticated else unauthenticated_client
    response = client.post(CARS_API_ENDPOINT, car_data)

    if authenticated:
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["brand"] == car_data["brand"]
        assert response.data["model"] == car_data["model"]
        assert response.data["year"] == car_data["year"]
        assert response.data["horse_power_count"] == car_data["horse_power_count"]
        assert response.data["color"] == car_data["color"]
    else:
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize("authenticated", [True, False])
def test_the_same_new_car(authenticated, user_supplier, authenticated_client, unauthenticated_client):
    client = authenticated_client if authenticated else unauthenticated_client
    response = client.post(CARS_API_ENDPOINT, car_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST if authenticated else status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize("authenticated", [True, False])
def test_update_car(authenticated, user_supplier, authenticated_client, unauthenticated_client):
    client = authenticated_client if authenticated else unauthenticated_client

    car = Car.objects.create(brand="BMW", model="M2", year=2023, horse_power_count=300.00, color="WHITE")

    updated_car_data = {
        "brand": "BMW",
        "model": "some Model",
        "year": 2023,
        "horse_power_count": 300.00,
        "color": "WHITE",
    }
    response = client.put(f"{CARS_API_ENDPOINT}{car.id}/", updated_car_data)

    if authenticated:
        assert response.status_code == status.HTTP_200_OK
        car.refresh_from_db()
        assert car.model == "some Model"
    else:
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize("authenticated", [True, False])
def test_delete_car(authenticated, user_supplier, authenticated_client, unauthenticated_client):
    client = authenticated_client if authenticated else unauthenticated_client

    car = Car.objects.create()

    response = client.delete(f"{CARS_API_ENDPOINT}{car.id}/")

    if authenticated:
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Car.objects.filter(is_active=True).count() == 0
    else:
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        car.refresh_from_db()
        assert Car.objects.filter(is_active=True).count() == 1
