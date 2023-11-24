from django.db import models
from djangoTask.src.core.models.abstract_models import Discount


class SupplierDiscount(Discount):
    supplier = models.ForeignKey('Supplier.Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class CarDealerDiscount(Discount):
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
