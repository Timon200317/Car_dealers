from django.db import models
from django.core.validators import MinValueValidator
from djangoTask.src.core.models.abstract_models import Base
from djangoTask.src.core.enums.enums import Color


class Brand(Base):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Model(Base):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    horse_power_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand.name} {self.name}"


class Car(Base):  # Certain car instance
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=10,
                             choices=[(color.value, color.name) for color in Color],
                             default=Color.WHITE.value
                             )

    def __str__(self):
        return f"{self.model} ({self.year})"


# Model for relationship between Car and Supplier
class CarSupplier(Base):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier.Supplier', on_delete=models.CASCADE)

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
        unique_together = ('car', 'supplier')


class CarDealerCar(Base):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
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
