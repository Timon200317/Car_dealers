import factory
from factory.django import DjangoModelFactory
from .specification_random import get_random_specification
from .user_factory import UserFactory
from djangoTask.src.apps.Client.models import Client


class ClientFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    client_name = factory.Faker('first_name')
    client_second_name = factory.Faker('last_name')
    phone_number = factory.Faker('phone_number')
    email = factory.Faker('email')
    balance = factory.Faker('random_number', digits=5)
    specification = get_random_specification()

    class Meta:
        model = Client
