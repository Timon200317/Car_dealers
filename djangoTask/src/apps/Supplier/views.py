from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .filters import SupplierFilter
from .serializers import SupplierSerializer, SupplierUniqueCarDealersSerializer, SupplierProfitSerializer, \
    SupplierCarsSerializer, SupplierCreateSerializer
from .models import Supplier, SupplierCars
from ..Car.models import Car
from ...core.tools.mixins import SafeDestroyModelMixin
from ...core.tools.permissions import IsSupplierAdminOrReadOnly


class SupplierCreateView(mixins.CreateModelMixin, GenericViewSet, SafeDestroyModelMixin):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class = SupplierCreateSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = SupplierFilter
    search_fields = ['supplier_name', 'year_of_origin']
    ordering_fields = ['id',
                       'supplier_name',
                       'year_of_origin',
                       ]


class SupplierViewSet(mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet, SafeDestroyModelMixin):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class = SupplierSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = SupplierFilter
    search_fields = ['supplier_name', 'year_of_origin']
    ordering_fields = ['id',
                       'supplier_name',
                       'year_of_origin',
                       ]

    @action(
        detail=True,
        methods=["post"],
        url_path="add-car",
        serializer_class=SupplierCarsSerializer,
    )
    def add_supplier_cars(self, request, pk=None):
        supplier = self.get_object()
        serializer = self.get_serializer(data=request.data, context={'supplier': supplier})
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                {"error": "This car already exists in this supplier"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        methods=["get"],
        detail=True,
        serializer_class=SupplierUniqueCarDealersSerializer,
        url_path="unique-car-dealers",
    )
    def unique_car_dealers(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"supplier_id": pk})

        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=True,
        serializer_class=SupplierProfitSerializer,
        url_path="profit",
    )
    def get_showroom_profit(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"supplier_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
