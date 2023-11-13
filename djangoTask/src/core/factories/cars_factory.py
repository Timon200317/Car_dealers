import random
from random import randint

from factory.django import DjangoModelFactory
import factory.fuzzy

from djangoTask.src.apps.CarDealer.models import CarDealer
from djangoTask.src.core.enums.enums import Color
from djangoTask.src.apps.Car.models import Car, CarDealerCar


class CarFactory(DjangoModelFactory):
    brand = factory.Faker('company')
    model = factory.Faker('word')
    horse_power_count = factory.Faker('random_int', min=100, max=500)
    year = factory.Faker('year')
    color = factory.Faker('random_element', elements=[choice[0] for choice in Color.choices])

    @classmethod
    def create(cls, model_class, user, cars=None, *args, **kwargs):
        car_dealer = CarDealer.objects.create(user=user, **kwargs)
        if cars:
            for car in cars:
                CarDealerCar.objects.create(
                    car=car,
                    car_dealer=car_dealer,
                    count=randint(1, 10),
                    price=round(random.uniform(40000, 10000000)),
                )
        return car_dealer

    class Meta:
        model = Car
