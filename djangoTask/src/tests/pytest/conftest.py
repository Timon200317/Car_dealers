import pytest
from django.core.management import call_command
from rest_framework.test import APIClient
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.tests.factories.user_factory import UserFactory


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        call_command('migrate')


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def authenticated_client():
    user = UserFactory(user_type=UserProfile.CLIENT)
    client.force_authenticate(user=user)
    yield client


@pytest.fixture
def unauthenticated_client():
    yield client
