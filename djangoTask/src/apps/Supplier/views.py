from rest_framework import viewsets

from .serializers import SupplierSerializer
from .models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
