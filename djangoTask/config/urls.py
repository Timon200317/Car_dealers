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
from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.CarDealer.views import CarDealerViewSet
from djangoTask.src.apps.Car.views import CarViewSet, BrandViewSet, ModelViewSet
from djangoTask.src.apps.Client.views import ClientViewSet
from djangoTask.src.apps.Supplier.views import SupplierViewSet
from djangoTask.src.apps.Promotion.views import SupplierPromotionViewSet, CarDealerPromotionViewSet
from djangoTask.src.apps.History.views import SupplierHistoryViewSet, ClientHistoryViewSet, CarDealerSalesHistoryViewSet
from djangoTask.src.apps.User.views import UserViewSet

router = DefaultRouter()
router.register(r'car_dealers', CarDealerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'models', ModelViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'users', UserViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplier_promotion', SupplierPromotionViewSet)
router.register(r'car_dealer_promotion', CarDealerPromotionViewSet)
router.register(r'supplier_history', SupplierHistoryViewSet)
router.register(r'car_dealer_history', CarDealerSalesHistoryViewSet)
router.register(r'client_history', ClientHistoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
