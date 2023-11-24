from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.Car.views import CarViewSet

router = DefaultRouter()

router.register(r'list', CarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

