from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import SupplierDiscountFilter, CarDealerDiscountFilter
from .serializers import CarDealerDiscountSerializer, SupplierDiscountSerializer
from .models import CarDealerDiscount, SupplierDiscount


class CarDealerDiscountViewSet(viewsets.ModelViewSet):
    queryset = CarDealerDiscount.objects.all()
    serializer_class = CarDealerDiscountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarDealerDiscountFilter


class SupplierDiscountViewSet(viewsets.ModelViewSet):
    queryset = SupplierDiscount.objects.all()
    serializer_class = SupplierDiscountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SupplierDiscountFilter


