from rest_framework import viewsets

from .serializers import CarDealerPromotionSerializer, SupplierPromotionSerializer
from .models import CarDealerPromotion, SupplierPromotion


class CarDealerPromotionViewSet(viewsets.ModelViewSet):
    queryset = CarDealerPromotion.objects.all()
    serializer_class = CarDealerPromotionSerializer


class SupplierPromotionViewSet(viewsets.ModelViewSet):
    queryset = SupplierPromotion.objects.all()
    serializer_class = SupplierPromotionSerializer


