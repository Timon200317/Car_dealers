from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .filters import SupplierDiscountFilter, CarDealerDiscountFilter
from .serializers import CarDealerDiscountSerializer, SupplierDiscountSerializer
from .models import CarDealerDiscount, SupplierDiscount


class CarDealerDiscountViewSet(viewsets.ModelViewSet):
    queryset = CarDealerDiscount.objects.all()
    serializer_class = CarDealerDiscountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarDealerDiscountFilter
    search_fields = ['name', 'description']
    ordering_fields = ['id',
                       'car_dealer',
                       'name',
                       'description',
                       'percent']


class SupplierDiscountViewSet(viewsets.ModelViewSet):
    queryset = SupplierDiscount.objects.all()
    serializer_class = SupplierDiscountSerializer
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = SupplierDiscountFilter
    search_fields = ['name', 'description']
    ordering_fields = ['id',
                       'supplier',
                       'name',
                       'description',
                       'percent']


