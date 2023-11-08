from rest_framework import viewsets

from .serializers import CarDealerSerializer
from .models import CarDealer


class CarDealerViewSet(viewsets.ModelViewSet):
    queryset = CarDealer.objects.all()
    serializer_class = CarDealerSerializer


