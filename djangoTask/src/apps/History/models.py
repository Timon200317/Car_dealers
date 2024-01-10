from django.db import models
from djangoTask.src.core.models.abstract_models import BaseHistory


class SalesDealerHistory(BaseHistory):  # Car Dealer History
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE, verbose_name='Car Dealer')

    class Meta:
        verbose_name = "Sales Dealer History"
        verbose_name_plural = "Sales Dealer Histories"


class SupplierSalesHistory(BaseHistory):  # Supplier History
    supplier = models.ForeignKey('Supplier.Supplier', on_delete=models.CASCADE)
    car_dealer = models.ForeignKey('CarDealer.CarDealer', on_delete=models.CASCADE, verbose_name='Car Dealer')

    class Meta:
        verbose_name = "Supplier Sales History"
        verbose_name_plural = "Supplier Sales Histories"
