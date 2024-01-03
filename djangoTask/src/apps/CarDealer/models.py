from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from djangoTask.src.core.models.abstract_models import Base
from djangoTask.src.apps.User.models import User
from django.core.validators import MinValueValidator
from django_countries.fields import CountryField
from djangoTask.src.apps.Car.models import Car, CarDealerCar


class CarDealer(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dealer_name = models.CharField(max_length=255, verbose_name='Car dealer name', unique=True)
    country = CountryField(null=True)
    balance = models.DecimalField(max_digits=12,decimal_places=2,
                                  validators=[MinValueValidator(0.00)],
                                  default=0.0
                                  )
    cars = models.ManyToManyField(Car, through=CarDealerCar)
    specification = models.JSONField(default=None, null=True, blank=True)

    def __str__(self):
        return self.dealer_name
