from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import GenericViewSet

from djangoTask.src.apps.User.filters import UserFilter
from djangoTask.src.apps.User.models import User
from djangoTask.src.apps.User.serializers import UserSerializer
from djangoTask.src.core.tools.mixins import SafeDestroyModelMixin


class UserViewSet(mixins.ListModelMixin,
                  GenericViewSet, SafeDestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = UserFilter
    search_fields = ['user_type']
    ordering_fields = ['id',
                       'user_type',
                       'first_name',
                       'last_name'
                       ]
