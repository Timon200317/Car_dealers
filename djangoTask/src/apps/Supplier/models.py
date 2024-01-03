import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from djangoTask.src.core.models.abstract_models import Base, Discount
from djangoTask.src.apps.User.models import User
from django_countries.fields import CountryField
from djangoTask.src.apps.Car.models import Car


class SupplierCars(Base):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        default=0.0,
    )
    price_with_discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        null=True,
    )

    def save(self, percent=None, *args, **kwargs):
        if percent:
            self.price_with_discount = self.price * (100 - percent) / 100
        else:
            self.price_with_discount = self.price
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("car", "supplier")


class Supplier(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255, unique=True)
    cars = models.ManyToManyField(Car, through=SupplierCars)
    year_of_origin = models.PositiveIntegerField(null=True,
                                                 validators=[
                                                     MinValueValidator(1700),
                                                     MaxValueValidator(int(datetime.date.today().year))
                                                 ]
                                                 )
    country = CountryField()

    def __str__(self):
        return self.supplier_name

    class Meta:
        ordering = ['supplier_name']
