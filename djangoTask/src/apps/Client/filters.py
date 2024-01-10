import django_filters
from .models import Client


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {
            "client_name": ["exact", "icontains"],
            "client_second_name": ["exact", "icontains"],
            "email": ["exact", "icontains"],
            "phone_number": ["exact"],
            "is_active": ["exact"]
        }
