from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .filters import SupplierFilter
from .serializers import SupplierSerializer
from .models import Supplier
from ...core.tools.mixins import SafeDestroyModelMixin
from ...core.tools.permissions import IsSupplierAdminOrReadOnly


class SupplierViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = SupplierFilter
    search_fields = ['supplier_name', 'year_of_origin']
    ordering_fields = ['id',
                       'supplier_name',
                       'year_of_origin',
                       ]



