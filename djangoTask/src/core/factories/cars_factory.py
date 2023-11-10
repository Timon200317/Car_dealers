from factory.django import DjangoModelFactory
import factory.fuzzy
from djangoTask.src.core.enums.enums import Color
from djangoTask.src.apps.Car.models import Brand, Model, Car


class BrandFactory(DjangoModelFactory):
    name = factory.Faker('company')

    class Meta:
        model = Brand


class ModelFactory(DjangoModelFactory):
    brand = factory.SubFactory(BrandFactory)
    name = factory.Faker('word')
    horse_power_count = factory.Faker('random_int', min=100, max=500)

    class Meta:
        model = Model


class CarFactory(DjangoModelFactory):
    model = factory.SubFactory(ModelFactory)
    year = factory.Faker('year')
    color = factory.Faker('random_element', elements=[choice[0] for choice in Color.choices])

    class Meta:
        model = Car
