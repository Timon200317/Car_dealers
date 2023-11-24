from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import SupplierSerializer
from .models import Supplier
from ..Car.models import Car, CarSupplier
from ...core.tools.mixins import SafeDestroyModelMixin
from ...core.tools.permissions import IsSupplierAdminOrReadOnly


class SupplierViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)

