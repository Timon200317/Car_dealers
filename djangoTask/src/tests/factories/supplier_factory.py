import random

import factory
from django_countries import countries
from factory.django import DjangoModelFactory
from djangoTask.src.apps.Supplier.models import Supplier
from .user_factory import UserFactory
from .cars_factory import CarFactory
from ...apps.History.models import SupplierSalesHistory


class SupplierFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    supplier_name = factory.Faker('company')
    year_of_origin = factory.Faker('pyint', min_value=1900, max_value=2023)

    class Meta:
        model = Supplier


class SupplierSalesHistoryFactory(DjangoModelFactory):
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    count = factory.Faker("pyint", min_value=1, max_value=100)

    @classmethod
    def _create(cls, model_class, car_dealer, supplier, car, *args, **kwargs):
        history = SupplierSalesHistory.objects.create(
            car_dealer=car_dealer, supplier=supplier, car=car, **kwargs
        )
        return history

    class Meta:
        model = SupplierSalesHistory

