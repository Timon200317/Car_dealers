from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Base(models.Model):  # Model with common fields
    is_active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BasePromotion(Base):
    name = models.CharField(max_length=255, verbose_name='Promotion name')
    description = models.TextField(blank=True, verbose_name='Promotion Description')
    start_date = models.DateTimeField(verbose_name='Promotion start date')
    end_date = models.DateTimeField(verbose_name='Promotion end date')
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Promotion percent',
                                              validators=[
                                                  MinValueValidator(0),
                                                  MaxValueValidator(100)
                                              ]
                                              )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.description}"


class BaseHistory(Base):
    date = models.DateField()
    count = models.PositiveIntegerField(verbose_name='Count')
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE, verbose_name='Car Dealer')
    car = models.ForeignKey('Car.Car', on_delete=models.CASCADE, verbose_name='Car')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.date} - {self.car.model} ({self.count})"
