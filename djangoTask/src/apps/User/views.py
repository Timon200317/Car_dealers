from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from djangoTask.src.apps.User.models import User
from djangoTask.src.apps.User.serializers import UserSerializer
from djangoTask.src.core.tools.mixins import SafeDestroyModelMixin


class UserViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
