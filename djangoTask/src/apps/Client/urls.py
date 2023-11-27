from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.Client.views import ClientViewSet

router = DefaultRouter()

router.register(r'list', ClientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
