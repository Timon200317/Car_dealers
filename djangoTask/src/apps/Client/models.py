from django.db import models
from djangoTask.src.core.models.abstract_models import Base


class Client(Base):
    client_name = models.CharField(max_length=255)
    client_second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.client_name


# Model for relationship between Client and CarDealer
class ClientCarDealer(Base):
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('client', 'car_dealer')
