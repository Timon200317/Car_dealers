import random

import factory
from django_countries import countries
from factory.django import DjangoModelFactory
from djangoTask.src.apps.Supplier.models import Supplier, CarSupplier
from .user_factory import UserFactory
from .cars_factory import CarFactory


class SupplierFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    supplier_name = factory.Faker('company')
    year_of_origin = factory.Faker('pyint', min_value=1900, max_value=2023)
    country = factory.Faker("random_element", elements=[country.name for country in countries])

    @classmethod
    def create(cls, user, cars=None, *args, **kwargs):
        supplier = Supplier.objects.create(user=user, **kwargs)
        if cars:
            for car in cars:
                CarSupplier.objects.create(
                    car=car,
                    supplier=supplier,
                    price=round(random.uniform(40000, 10000000)),
                )
        return supplier

    class Meta:
        model = Supplier


class CarSupplierFactory(DjangoModelFactory):
    car = factory.SubFactory(CarFactory)
    supplier = factory.SubFactory(SupplierFactory)
    price = factory.Faker('random_int', min=1000, max=10000)

    class Meta:
        model = CarSupplier
