from django.shortcuts import get_object_or_404
from django_filters import OrderingFilter
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, mixins
from rest_framework.viewsets import GenericViewSet

from .filters import CarDealerFilter
from .serializers import CarDealerSerializer, CarDealerProfitSerializer, CarDealerNumberOfSellsSerializer, \
    CarDealerUniqueSuppliersSerializer, CarDealerUniqueClientsSerializer, CarDealerCarsSerializer, \
    CarDealerCreateSerializer
from .models import CarDealer
from djangoTask.src.core.tools.permissions import IsCarDealerAdminOrReadOnly
from ..Car.models import Car, CarDealerCar
from ...core.tools.mixins import SafeDestroyModelMixin


class CarDealerCreateView(mixins.CreateModelMixin,
                          GenericViewSet, SafeDestroyModelMixin):
    queryset = CarDealer.objects.filter(is_active=True)
    serializer_class = CarDealerCreateSerializer
    permission_classes = (IsCarDealerAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    filterset_class = CarDealerFilter
    search_fields = ['dealer_name', 'country']
    ordering_fields = ['id',
                       'dealer_name',
                       'country']


class CarDealerViewSet(mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet, SafeDestroyModelMixin):
    queryset = CarDealer.objects.filter(is_active=True)
    serializer_class = CarDealerSerializer
    permission_classes = (IsCarDealerAdminOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    filterset_class = CarDealerFilter
    search_fields = ['dealer_name', 'country']
    ordering_fields = ['id',
                       'dealer_name',
                       'country']

    @action(
        detail=True,
        methods=["post"],
        url_path="add-car",
        serializer_class=CarDealerCarsSerializer,
    )
    def add_car_dealer_cars(self, request, pk=None):
        car_dealer = self.get_object()
        serializer = self.get_serializer(data=request.data, context={'car_dealer': car_dealer})
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                {"error": "This car already exists in this car dealer"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        methods=["get"],
        detail=True,
        serializer_class=CarDealerUniqueClientsSerializer,
        url_path="unique-clients",
    )
    def get_unique_clients(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"car_dealer_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=True,
        serializer_class=CarDealerUniqueSuppliersSerializer,
        url_path="unique-suppliers",
    )
    def get_unique_suppliers(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"car_dealer_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=True,
        serializer_class=CarDealerNumberOfSellsSerializer,
        url_path="number-of-sell",
    )
    def get_number_of_sells(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"car_dealer_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=True,
        serializer_class=CarDealerProfitSerializer,
        url_path="profit",
    )
    def get_showroom_profit(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, context={"car_dealer_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
