from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import GenericViewSet

from .filters import SalesDealerHistoryFilter, SupplierSalesHistoryFilter
from .serializers import SalesDealerHistorySerializer, SupplierSalesHistorySerializer
from .models import SalesDealerHistory, SupplierSalesHistory
from djangoTask.src.core.tools.permissions import IsCarDealerAdminOrReadOnly, \
    IsSupplierAdminOrReadOnly
from ...core.tools.mixins import SafeDestroyModelMixin


class CarDealerSalesHistoryViewSet(mixins.ListModelMixin, SafeDestroyModelMixin, GenericViewSet):
    queryset = SalesDealerHistory.objects.filter(is_active=True)
    serializer_class = SalesDealerHistorySerializer
    permission_classes = (IsCarDealerAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = SalesDealerHistoryFilter
    search_fields = ['date', 'price']
    ordering_fields = ['id',
                       'date',
                       'price',
                       'car',
                       'count',
                       'percent']


class SupplierHistoryViewSet(mixins.ListModelMixin,
                             GenericViewSet, SafeDestroyModelMixin):
    queryset = SupplierSalesHistory.objects.filter(is_active=True)
    serializer_class = SupplierSalesHistorySerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = SupplierSalesHistoryFilter
    search_fields = ['date', 'price']
    ordering_fields = ['id',
                       'date',
                       'price',
                       'car',
                       'count',
                       'percent']
