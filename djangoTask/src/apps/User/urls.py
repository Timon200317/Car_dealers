from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.User.views import UserViewSet

router = DefaultRouter()

router.register(r'list', UserViewSet)

urlpatterns = router.urls
