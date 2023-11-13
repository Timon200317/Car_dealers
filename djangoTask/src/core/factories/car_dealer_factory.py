import factory
from django_countries import countries
import random
from djangoTask.src.apps.Car.models import CarDealerCar
from djangoTask.src.apps.CarDealer.models import CarDealer
from djangoTask.src.apps.User.models import User
from djangoTask.src.core.enums.enums import UserProfile
from djangoTask.src.core.factories.specification_random import get_random_specification
from djangoTask.src.core.factories.user_factory import UserFactory


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

