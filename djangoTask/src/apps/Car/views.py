from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .filters import CarFilter
from .serializers import CarSerializer
from .models import Car
from djangoTask.src.core.tools.permissions import IsSupplierAdminOrReadOnly
from ...core.tools.mixins import SafeDestroyModelMixin


class CarViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    filterset_class = CarFilter
    search_fields = ['brand', 'model']
    ordering_fields = ['id',
                       'brand',
                       'model',
                       'year',
                       'horse_power_count'
                       ]


