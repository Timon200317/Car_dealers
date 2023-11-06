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
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0)]
                                )
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

    class Meta:
        unique_together = ('car', 'supplier')
