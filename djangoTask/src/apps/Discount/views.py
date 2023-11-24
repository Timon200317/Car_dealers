from rest_framework import viewsets

from .serializers import CarDealerDiscountSerializer, SupplierDiscountSerializer
from .models import CarDealerDiscount, SupplierDiscount


class CarDealerDiscountViewSet(viewsets.ModelViewSet):
    queryset = CarDealerDiscount.objects.all()
    serializer_class = CarDealerDiscountSerializer


class SupplierDiscountViewSet(viewsets.ModelViewSet):
    queryset = SupplierDiscount.objects.all()
    serializer_class = SupplierDiscountSerializer


