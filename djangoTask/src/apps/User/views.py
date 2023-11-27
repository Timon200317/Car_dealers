from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from djangoTask.src.apps.User.filters import UserFilter
from djangoTask.src.apps.User.models import User
from djangoTask.src.apps.User.serializers import UserSerializer
from djangoTask.src.core.tools.mixins import SafeDestroyModelMixin


class UserViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
