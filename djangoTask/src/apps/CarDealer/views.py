from rest_framework import viewsets
from .serializers import CarDealerSerializer
from .models import CarDealer
from djangoTask.src.core.tools.permissions import IsCarDealerAdminOrReadOnly
from ...core.tools.mixins import SafeDestroyModelMixin


class CarDealerViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = CarDealer.objects.filter(is_active=True)
    serializer_class = CarDealerSerializer
    permission_classes = (IsCarDealerAdminOrReadOnly,)



