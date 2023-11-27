from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import SalesDealerHistoryFilter, SupplierSalesHistoryFilter
from .serializers import SalesDealerHistorySerializer, SupplierSalesHistorySerializer
from .models import SalesDealerHistory, SupplierSalesHistory
from djangoTask.src.core.tools.permissions import IsCarDealerAdmin, IsSupplierAdmin
from ...core.tools.mixins import SafeDestroyModelMixin


class CarDealerSalesHistoryViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = SalesDealerHistory.objects.filter(is_active=True)
    serializer_class = SalesDealerHistorySerializer
    permission_classes = (IsCarDealerAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SalesDealerHistoryFilter


class SupplierHistoryViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = SupplierSalesHistory.objects.filter(is_active=True)
    serializer_class = SupplierSalesHistorySerializer
    permission_classes = (IsSupplierAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SupplierSalesHistoryFilter

