from django.db import models
from djangoTask.src.core.models.abstract_models import BaseHistory


class SalesDealerHistory(BaseHistory):  # Car Dealer History
    class Meta:
        verbose_name = "Sales Dealer History"
        verbose_name_plural = "Sales Dealer Histories"


class PurchaseHistory(BaseHistory):  # Client History
    class Meta:
        verbose_name = "Purchase History"
        verbose_name_plural = "Purchase Histories"


class SupplierSalesHistory(BaseHistory):  # Supplier History
    supplier = models.ForeignKey('Supplier.Supplier', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Supplier Sales History"
        verbose_name_plural = "Supplier Sales Histories"
