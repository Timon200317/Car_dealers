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


router = DefaultRouter()
router.register(r'api/car_dealers', CarDealerViewSet)
router.register(r'api/cars', CarViewSet)
router.register(r'api/models', ModelViewSet)
router.register(r'api/brands', BrandViewSet)
router.register(r'api/clients', ClientViewSet)
router.register(r'api/suppliers', SupplierViewSet)
# router.register(r'api/supplier_promotion', SupplierPromotionViewSet)
# router.register(r'api/car_dealer_promotion', CarDealerPromotionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
