from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.CarDealer.views import CarDealerViewSet, CarDealerCreateView
from djangoTask.src.apps.Discount.views import CarDealerDiscountViewSet
from djangoTask.src.apps.History.views import CarDealerSalesHistoryViewSet

router = DefaultRouter()

router.register(r'list', CarDealerViewSet)
router.register(r'create', CarDealerCreateView)
router.register(r'discounts', CarDealerDiscountViewSet)
router.register(r'history', CarDealerSalesHistoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
