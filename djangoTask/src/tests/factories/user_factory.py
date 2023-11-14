import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from djangoTask.src.core.enums.enums import UserProfile


class UserFactory(DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    user_type = factory.Faker('random_element', elements=[choice[0] for choice in UserProfile.choices])

    class Meta:
        model = get_user_model()
