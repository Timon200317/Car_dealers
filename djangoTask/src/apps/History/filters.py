import django_filters
from django_filters import DateFilter

from .models import SalesDealerHistory, SupplierSalesHistory


class SalesDealerHistoryFilter(django_filters.FilterSet):
    date = DateFilter(field_name='date', lookup_expr='exact')

    class Meta:
        model = SalesDealerHistory
        fields = {
            "car_dealer": ["exact"],
            "date": ["exact", "year", "month", "day", "week_day", "range", "gt", "lt"],
            "count": ["exact", "gte", "lte"],
            "price": ["exact", "gte", "lte"],
        }


class SupplierSalesHistoryFilter(django_filters.FilterSet):
    date = DateFilter(field_name='date', lookup_expr='exact')

    class Meta:
        model = SupplierSalesHistory
        fields = {
            "supplier": ["exact"],
            "date": ["exact", "year", "month", "day", "week_day", "range", "gt", "lt"],
            "count": ["exact", "gte", "lte"],
            "price": ["exact", "gte", "lte"],
        }
