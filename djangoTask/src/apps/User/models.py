from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_car_dealer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
