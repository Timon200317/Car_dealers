import django_filters
from .models import SupplierDiscount, CarDealerDiscount


class SupplierDiscountFilter(django_filters.FilterSet):
    class Meta:
        model = SupplierDiscount
        fields = {
            "supplier": ["exact"],
            "percent": ["exact", "gte", "lte"],
            "date_start": ["exact", "gte", "lte"],
            "date_end": ["exact", "gte", "lte"],
        }


class CarDealerDiscountFilter(django_filters.FilterSet):
    class Meta:
        model = CarDealerDiscount
        fields = {
            "car_dealer": ["exact"],
            "percent": ["exact", "gte", "lte"],
            "date_start": ["exact", "gte", "lte"],
            "date_end": ["exact", "gte", "lte"],
        }
