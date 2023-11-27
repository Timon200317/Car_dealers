import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            "brand": ["exact", "icontains"],
            "model": ["exact", "icontains"],
            "color": ["exact", "icontains"],
            "horse_power_count": ["exact", "gte", "lte"],
            "year": ["exact", "gte", "lte"],
        }

