from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filters import SupplierFilter
from .serializers import SupplierSerializer
from .models import Supplier
from ...core.tools.mixins import SafeDestroyModelMixin
from ...core.tools.permissions import IsSupplierAdminOrReadOnly


class SupplierViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SupplierFilter

