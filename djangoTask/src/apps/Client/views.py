from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .filters import ClientFilter
from .serializers import ClientSerializer
from .models import Client
from ...core.tools.permissions import IsClientAdminOrReadOnly
from ...core.tools.mixins import SafeDestroyModelMixin


class ClientViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsClientAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = ClientFilter
    search_fields = ['client_name', 'client_second_name', 'email']
    ordering_fields = ['id',
                       'client_name',
                       'client_second_name',
                       'email',
                       'phone_number']
