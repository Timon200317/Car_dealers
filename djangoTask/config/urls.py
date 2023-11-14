"""
URL configuration for djangoTask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.CarDealer.views import CarDealerViewSet
from djangoTask.src.apps.Car.views import CarViewSet
from djangoTask.src.apps.Client.views import ClientViewSet
from djangoTask.src.apps.Supplier.views import SupplierViewSet
from djangoTask.src.apps.Discount.views import SupplierDiscountViewSet, CarDealerDiscountViewSet
from djangoTask.src.apps.History.views import SupplierHistoryViewSet, ClientHistoryViewSet, CarDealerSalesHistoryViewSet
from djangoTask.src.apps.User.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="CarDealer API",
        default_version='v1',
        description="API for CarDealer project on Django REST",
        contact=openapi.Contact(email="timofeysidorenko03@gmail.com"),
    ),
    public=True,
    permission_classes=[AllowAny,],
)

router = DefaultRouter()
router.register(r'car_dealers', CarDealerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'users', UserViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplier_promotion', SupplierDiscountViewSet)
router.register(r'car_dealer_promotion', CarDealerDiscountViewSet)
router.register(r'supplier_history', SupplierHistoryViewSet)
router.register(r'car_dealer_history', CarDealerSalesHistoryViewSet)
router.register(r'client_history', ClientHistoryViewSet)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
