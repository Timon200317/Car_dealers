from factory.django import DjangoModelFactory
import factory.fuzzy
from djangoTask.src.core.enums.enums import Color
from djangoTask.src.apps.Car.models import Car


class CarFactory(DjangoModelFactory):
    brand = factory.Faker('company')
    model = factory.Faker('word')
    horse_power_count = factory.Faker('random_int', min=100, max=500)
    year = factory.Faker('year')
    color = factory.Faker('random_element', elements=[choice[0] for choice in Color.choices])

    class Meta:
        model = Car
