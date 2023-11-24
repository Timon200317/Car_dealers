from rest_framework.routers import DefaultRouter
from djangoTask.src.apps.User.views import UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = router.urls
