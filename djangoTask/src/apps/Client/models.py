from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from djangoTask.src.core.models.abstract_models import Base
from djangoTask.src.apps.User.models import User
from django.core.validators import MinLengthValidator, EmailValidator, MaxLengthValidator
from django.core.validators import MinValueValidator


class Client(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    client_second_name = models.CharField(max_length=255)
    phone_number = models.CharField(
                                    validators=[MinLengthValidator(limit_value=10),
                                                MaxLengthValidator(limit_value=15)])
    email = models.CharField(max_length=255,
                             validators=[MinLengthValidator(limit_value=11),
                                         EmailValidator(message='Enter a valid email address.')]
                             )
    balance = models.DecimalField(default=0.0, verbose_name='Client balance',
                                  validators=[MinValueValidator(0.0)],
                                  decimal_places=2,
                                  max_digits=12
                                  )
    specification = models.JSONField(default=None, null=True, blank=True)

    def __str__(self):
        return self.client_name


# Model for relationship between Client and CarDealer
class ClientCarDealer(Base):
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('client', 'car_dealer')
