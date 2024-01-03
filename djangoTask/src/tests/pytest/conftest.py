import pytest
from django.core.management import call_command
from rest_framework.test import APIClient
from djangoTask.src.apps.User.models import User
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.tests.factories.user_factory import UserFactory


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        call_command('migrate')


@pytest.fixture
def car_data():
    return {
        "brand": "BMW",
        "model": "M2",
        "year": 2023,
        "horse_power_count": 300.00,
        "color": "WHITE",
    }


@pytest.fixture
def user_supplier():
    return User.objects.create_user(
        username='supplier',
        password='testpass',
        user_type='SUPPLIER'
    )


@pytest.fixture
def authenticated_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def unauthenticated_client():
    return APIClient()
