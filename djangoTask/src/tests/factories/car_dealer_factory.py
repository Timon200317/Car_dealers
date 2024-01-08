import factory
from django_countries import countries
import random

from factory.django import DjangoModelFactory

from djangoTask.src.apps.Car.models import CarDealerCar
from djangoTask.src.apps.CarDealer.models import CarDealer
from djangoTask.src.apps.History.models import SalesDealerHistory
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.tests.factories.specification_random import get_random_specification
from djangoTask.src.tests.factories.user_factory import UserFactory


class CarDealerFactory(factory.django.DjangoModelFactory):
    user = UserFactory(user_type=UserProfile.CAR_DEALER)
    dealer_name = factory.Faker('company')
    country = factory.Faker("random_element", elements=[x for x in countries])
    balance = factory.Faker('random_number', digits=5)
    specification = get_random_specification()

    @classmethod
    def create(cls, user, cars=None, *args, **kwargs):
        car_dealer = CarDealer.objects.create(user=user, **kwargs)
        if cars:
            for car in cars:
                CarDealerCar.objects.create(
                    car=car,
                    car_dealer=car_dealer,
                    count=random.randint(1, 100),
                    price=round(random.uniform(40000, 10000000)),
                )
        return car_dealer

    class Meta:
        model = CarDealer


class CarDealerSalesHistoryFactory(DjangoModelFactory):
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    count = factory.Faker("pyint", min_value=1, max_value=100)

    @classmethod
    def _create(cls, model_class, car_dealer, client, car, *args, **kwargs):
        history = SalesDealerHistory.objects.create(
            car_dealer=car_dealer, client=client, car=car, **kwargs
        )
        return history

    class Meta:
        model = SalesDealerHistory
