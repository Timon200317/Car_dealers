import django_filters
from .models import CarDealer


class CarDealerFilter(django_filters.FilterSet):
    class Meta:
        model = CarDealer
        fields = {
            "dealer_name": ["exact", "icontains"],
            "country": ["exact", "icontains"],
            "is_active": ["exact"],
        }
