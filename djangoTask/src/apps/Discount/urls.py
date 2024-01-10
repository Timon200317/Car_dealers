from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.Car.views import CarViewSet
from djangoTask.src.apps.Discount.views import SupplierDiscountDetailView, SupplierDiscountViewSet, \
    CarDealerDiscountViewSet, SupplierDiscountListView

router = DefaultRouter()

router.register("cardealerdiscounts", CarDealerDiscountViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "supplierdiscounts/<int:pk>/",
        SupplierDiscountDetailView.as_view(),
        name="supplierdiscountdetail",
    ),
    path(
        "supplierdiscounts/",
        SupplierDiscountListView.as_view(),
        name="providerdiscountslist",
    ),
]