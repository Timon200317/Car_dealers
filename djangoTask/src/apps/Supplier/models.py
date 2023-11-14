from django.db import models
from djangoTask.src.core.models.abstract_models import Base, Discount
from djangoTask.src.apps.User.models import User
from django_countries.fields import CountryField
from djangoTask.src.apps.Car.models import Car, CarSupplier


class Supplier(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255, unique=True)
    cars = models.ManyToManyField(Car, through=CarSupplier)
    year_of_origin = models.PositiveIntegerField(null=True)
    country = CountryField()

    def __str__(self):
        return self.supplier_name

    class Meta:
        ordering = ['supplier_name']


