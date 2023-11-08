from rest_framework import viewsets

from .serializers import CarDealerPromotionSerializer, SupplierPromotionSerializer
from .models import CarDealerPromotion, SupplierPromotion


class CarDealerViewSet(viewsets.ModelViewSet):
    queryset = CarDealerPromotion.objects.all()
    serializer_class = CarDealerPromotionSerializer
