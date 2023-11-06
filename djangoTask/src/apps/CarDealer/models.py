from django.db import models
from djangoTask.src.core.models.abstract_models import Base
from django.core.validators import MinValueValidator
from django_countries.fields import CountryField


class CarDealer(Base):
    dealer_name = models.CharField(max_length=255, verbose_name='Car dealer name')
    country = CountryField()
    balance = models.FloatField(default=0, verbose_name='Car Dealer balance',
                                validators=[MinValueValidator(0)]
                                )

    def __str__(self):
        return self.dealer_name


# Model for relationship between CarDealer and Supplier
class CarDealerSupplier(Base):
    car_dealer = models.ForeignKey('CarDealer', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier.Supplier', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('car_dealer', 'supplier')
