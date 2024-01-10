import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            "first_name": ["exact", "icontains"],
            "last_name": ["exact", "icontains"],
            "is_active": ["exact"],
        }
