import django_filters
from .models import Supplier


class SupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fields = {
            "supplier_name": ["exact", "icontains"],
            "year_of_origin": ["exact", "icontains"],
            "is_active": ["exact"]
        }
