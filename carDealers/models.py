from django.db import models
from enum import Enum
from django_countries.fields import CountryField


# --------------Enum-----------------
class Color(Enum):
    RED = 'Red'
    BLUE = 'Blue'
    GREEN = 'Green'
    YELLOW = 'Yellow'
    WHITE = 'White'
    BLACK = 'Black'
    SILVER = 'Silver'
    GRAY = 'Gray'


# ------------------------------------------------------------------------------------------------------
# --------Abstract classes------------
class Base(models.Model):  # Model with common fields
    is_active = models.BooleanField(default=True)
    last_update_time = models.TimeField(verbose_name='Last update instance time')
    creation_time = models.TimeField(verbose_name='Last update instance time')

    class Meta:
        abstract = True


class BasePromotion(Base):
    name = models.CharField(max_length=255, verbose_name='Promotion name')
    description = models.TextField(verbose_name='Promotion Description')
    start_date = models.DateField(verbose_name='Promotion start date')
    end_date = models.DateField(verbose_name='Promotion end date')
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Promotion percent')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.description}"


class BaseHistory(Base):
    date = models.DateField()
    count = models.PositiveIntegerField(max_length=100, verbose_name='Count')
    car_dealer = models.ForeignKey('CarDealer', on_delete=models.CASCADE, verbose_name='Car Dealer')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='Car')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.date} - {self.car.model} ({self.count})"


# ------------------------------------------------------------------------------------------------------
# Car Dealer Section Models
class CarDealer(Base):
    dealer_name = models.CharField(max_length=255, verbose_name='Car dealer name')
    country = CountryField()
    balance = models.FloatField(default=0, verbose_name='Car Dealer balance')

    def __str__(self):
        return self.dealer_name


# Model for relationship between CarDealer and Supplier
class CarDealerSupplier(Base):
    car_dealer = models.ForeignKey('CarDealer', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('car_dealer', 'supplier')


class SalesDealerHistory(BaseHistory):  # Car Dealer History
    class Meta:
        verbose_name = "Sales Dealer History"
        verbose_name_plural = "Sales Dealer Histories"


class Brand(Base):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Model(Base):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    horse_power_count = models.PositiveIntegerField()
    color = models.CharField(max_length=10,
                             choices=[(color.value, color.name) for color in Color],
                             default=Color.WHITE.value
                             )

    def __str__(self):
        return f"{self.brand.name} {self.name}"


class Car(Base):  # Certain car instance
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.model} ({self.year})"


# Model for relationship between Car and Supplier
class CarSupplier(Base):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('car', 'supplier')


class CarDealerPromotion(BasePromotion):
    car_dealer = models.ForeignKey('CarDealer', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='Car')

    class Meta:
        verbose_name = "Car Dealer Promotion"
        verbose_name_plural = "Car Dealer Promotions"


# ------------------------------------------------------------------------------------------------------
# Client Section Models
class Client(Base):
    client_name = models.CharField(max_length=255)
    client_second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    registration_date = models.DateTimeField()

    def __str__(self):
        return self.client_name


class PurchaseHistory(BaseHistory):  # Client History
    class Meta:
        verbose_name = "Purchase History"
        verbose_name_plural = "Purchase Histories"


# Model for relationship between Client and CarDealer
class ClientCarDealer(Base):
    car_dealer = models.ForeignKey('CarDealer', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('client', 'car_dealer')


# ------------------------------------------------------------------------------------------------------
# Supplier Section Models
class Supplier(Base):
    supplier_name = models.CharField(max_length=255)
    year_of_origin = models.PositiveIntegerField(max_length=4)
    country = CountryField()


class SupplierSalesHistory(BaseHistory):  # Supplier History
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Supplier Sales History"
        verbose_name_plural = "Supplier Sales Histories"


class SupplierPromotion(BasePromotion):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    car_dealer = models.ForeignKey('CarDealer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Supplier Promotion"
        verbose_name_plural = "Supplier Promotions"
