from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.Client.views import ClientViewSet
from djangoTask.src.apps.History.views import ClientHistoryViewSet

router = DefaultRouter()

router.register(r'list', ClientViewSet)
router.register(r'history', ClientHistoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
