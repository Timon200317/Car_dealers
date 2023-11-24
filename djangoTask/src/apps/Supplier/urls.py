from django.urls import include, path
from rest_framework.routers import DefaultRouter

from djangoTask.src.apps.Discount.views import SupplierDiscountViewSet
from djangoTask.src.apps.History.views import SupplierHistoryViewSet
from djangoTask.src.apps.Supplier.views import SupplierViewSet

router = DefaultRouter()

router.register(r'list', SupplierViewSet)
router.register(r'discounts', SupplierDiscountViewSet)
router.register(r'history', SupplierHistoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


