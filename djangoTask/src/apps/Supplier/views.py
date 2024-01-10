from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from .filters import SupplierFilter
from .serializers import SupplierSerializer, SupplierUniqueCarDealersSerializer, SupplierProfitSerializer
from .models import Supplier, SupplierCars
from ..Car.models import Car
from ...core.tools.mixins import SafeDestroyModelMixin
from ...core.tools.permissions import IsSupplierAdminOrReadOnly


class SupplierViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = Supplier.objects.all()
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
    )
    def add_provider_cars(self, request, pk=None):
        supplier = self.get_object()
        car_id = request.data.get("car_id")

        car = get_object_or_404(Car, pk=car_id)

        price = request.data.get("price")
        try:
            SupplierCars.objects.create(car=car, supplier=supplier, price=price)
        except IntegrityError:
            return Response(
                {"error": "This car already exists in this provider"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_200_OK)

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



