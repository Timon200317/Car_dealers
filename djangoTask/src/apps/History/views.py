from rest_framework.permissions import IsAuthenticated
from .serializers import ClientHistorySerializer, SalesDealerHistorySerializer, SupplierSalesHistorySerializer
from .models import PurchaseHistory, SalesDealerHistory, SupplierSalesHistory
from djangoTask.src.core.tools.permissions import IsCarDealerAdmin, IsSupplierAdmin
from djangoTask.src.apps.CarDealer.views import BaseViewSet


class CarDealerSalesHistoryViewSet(BaseViewSet):
    queryset = SalesDealerHistory.objects.filter(is_active=True)
    serializer_class = SalesDealerHistorySerializer
    permission_classes = (IsCarDealerAdmin,)


class ClientHistoryViewSet(BaseViewSet):
    queryset = PurchaseHistory.objects.filter(is_active=True)
    serializer_class = ClientHistorySerializer
    permission_classes = (IsAuthenticated,)


class SupplierHistoryViewSet(BaseViewSet):
    queryset = SupplierSalesHistory.objects.filter(is_active=True)
    serializer_class = SupplierSalesHistorySerializer
    permission_classes = (IsSupplierAdmin,)

