import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from djangoTask.src.core.models.abstract_models import Base
from djangoTask.src.core.enums.enums import Color


class Car(Base):  # Certain car instance
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    horse_power_count = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    year = models.PositiveIntegerField(
        default=int(datetime.date.today().year),
        validators=[MaxValueValidator(int(datetime.date.today().year) + 1)])
    color = models.CharField(
        choices=Color.choices, max_length=8, default=Color.WHITE
    )

    def __str__(self):
        return f"{self.brand} {self.model} - {self.year}({self.color})"

    class Meta:
        unique_together = ('brand', 'model', 'horse_power_count', 'year', 'color')


class CarDealerCar(Base):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
    )
    price_with_discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
    )

    def save(self, percent=None, *args, **kwargs):
        if percent:
            self.price_with_discount = self.price * (100 - percent) / 100
        else:
            self.price_with_discount = self.price
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('car', 'car_dealer')
