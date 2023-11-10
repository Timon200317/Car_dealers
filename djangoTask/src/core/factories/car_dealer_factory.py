import factory
from django_countries import countries
from djangoTask.src.apps.CarDealer.models import CarDealer
from djangoTask.src.core.factories.cars_factory import CarFactory
from djangoTask.src.core.factories.specification_random import get_random_specification
from djangoTask.src.core.factories.user_factory import UserFactory


class CarDealerFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    dealer_name = factory.Faker('company')
    country = factory.Faker("random_element", elements=[x for x in countries])
    balance = factory.Faker('random_number', digits=5)
    specification = get_random_specification()
    cars = factory.RelatedFactory(CarFactory, through='CarDealerCarFactory')

    class Meta:
        model = CarDealer

