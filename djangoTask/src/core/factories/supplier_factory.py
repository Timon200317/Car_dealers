import factory
from django_countries import countries
from factory.django import DjangoModelFactory
from djangoTask.src.apps.Supplier.models import Supplier, CarSupplier
from .user_factory import UserFactory
from .cars_factory import CarFactory


class CarSupplierFactory(DjangoModelFactory):
    car = factory.SubFactory(CarFactory)
    supplier = factory.SubFactory('SupplierFactory')
    price = factory.Faker('random_int', min=1000, max=10000)

    class Meta:
        model = CarSupplier


class SupplierFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    supplier_name = factory.Faker('company')
    year_of_origin = factory.Faker('random_int', min=1900, max=2023)
    country = factory.Faker("random_element", elements=[x for x in countries])
    cars = factory.RelatedFactory(CarFactory, through='CarSupplierFactory')   # ManyToManyField

    class Meta:
        model = Supplier
