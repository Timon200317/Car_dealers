from django.db import models
from djangoTask.src.core.models.abstract_models import BasePromotion


class CarDealerPromotion(BasePromotion):
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE)
    car = models.ForeignKey('Car.Car', on_delete=models.CASCADE, verbose_name='Car')

    class Meta:
        verbose_name = "Car Dealer Promotion"
        verbose_name_plural = "Car Dealer Promotions"


class SupplierPromotion(BasePromotion):
    supplier = models.ForeignKey('Supplier.Supplier', on_delete=models.CASCADE)
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Supplier Promotion"
        verbose_name_plural = "Supplier Promotions"
