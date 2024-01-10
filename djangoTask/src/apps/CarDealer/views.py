from django_filters import OrderingFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import CarDealerFilter
from .serializers import CarDealerSerializer
from .models import CarDealer
from djangoTask.src.core.tools.permissions import IsCarDealerAdminOrReadOnly
from ...core.tools.mixins import SafeDestroyModelMixin


class CarDealerViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = CarDealer.objects.filter(is_active=True)
    serializer_class = CarDealerSerializer
    permission_classes = (IsCarDealerAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    filterset_class = CarDealerFilter
    search_fields = ['dealer_name', 'country']
    ordering_fields = ['id',
                       'dealer_name',
                       'country']



