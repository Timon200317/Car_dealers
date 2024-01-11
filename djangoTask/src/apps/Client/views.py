from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .filters import ClientFilter
from .serializers import ClientSerializer, ClientTotalAmountSpentSerializer, ClientCarsListSerializer, \
    ClientCreateSerializer
from .models import Client
from ...core.tools.permissions import IsClientAdminOrReadOnly
from ...core.tools.mixins import SafeDestroyModelMixin


class ClientViewSet(mixins.ListModelMixin,
                    GenericViewSet, SafeDestroyModelMixin):
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

    @action(
        detail=True,
        methods=["post"],
        url_path="create-client",
        serializer_class=ClientCreateSerializer,
    )
    def create_client(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(
                {"error": "This client already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        methods=["get"],
        detail=True,
        serializer_class=ClientTotalAmountSpentSerializer,
        url_path="total-amount-spent",
    )
    def get_total_client_spent(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"client_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=True,
        serializer_class=ClientCarsListSerializer,
        url_path="client-cars",
    )
    def bought_cars(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"client_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
