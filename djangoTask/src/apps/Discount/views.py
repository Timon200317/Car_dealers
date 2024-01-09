from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import SupplierDiscountFilter, CarDealerDiscountFilter
from .serializers import CarDealerDiscountSerializer, SupplierDiscountSerializer
from .models import CarDealerDiscount, SupplierDiscount
from ..Car.models import CarDealerCar
from ..Supplier.models import SupplierCars
from ...core.tools.functions import find_cars_by_specification
from ...core.tools.permissions import IsSupplierAdminOrReadOnly


class CarDealerDiscountViewSet(viewsets.ModelViewSet):
    queryset = CarDealerDiscount.objects.all()
    serializer_class = CarDealerDiscountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarDealerDiscountFilter
    search_fields = ['name', 'description']
    ordering_fields = ['id',
                       'car_dealer',
                       'name',
                       'description',
                       'percent']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        car_dealer = request.data["car_dealer"]
        cars = find_cars_by_specification(request.data["params"])
        percent = request.data["percent"]
        for car in cars:
            car_dealer_car_price = (
                CarDealerCar.objects.filter(car_dealer__id=car_dealer)
                .select_related("car")
                .get(car__id=car.id)
            )
            car_dealer_car_price.save(percent=percent)

        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        instance = self.get_object()
        car_dealer = instance.car_dealer
        cars = find_cars_by_specification(instance.params)
        percent = instance.percent
        for car in cars:
            car_dealer_car_price = (
                CarDealerCar.objects.filter(car_dealer__id=car_dealer.id)
                .select_related("car")
                .get(car__id=car.id)
            )
            car_dealer_car_price.save(percent=percent)
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        car_dealer = instance.car_dealer
        cars = find_cars_by_specification(instance.params)
        for car in cars:
            car_dealer_car_price = (
                CarDealerCar.objects.filter(car_dealer__id=car_dealer.id)
                .select_related("car")
                .get(car__id=car.id)
            )
            car_dealer_car_price.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SupplierDiscountViewSet(viewsets.ModelViewSet):
    queryset = SupplierDiscount.objects.all()
    serializer_class = SupplierDiscountSerializer
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_class = SupplierDiscountFilter
    search_fields = ['name', 'description']
    ordering_fields = ['id',
                       'supplier',
                       'name',
                       'description',
                       'percent']

    def get(self, request):
        discount = SupplierDiscount.objects.filter(is_active=True)
        serializer = SupplierDiscountSerializer(instance=discount, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierDiscountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            provider = request.data["provider"]
            cars = find_cars_by_specification(request.data["params"])
            percent = request.data["percent"]
            for car in cars:
                provider_car_price = (
                    SupplierCars.objects.filter(provider__id=provider)
                    .select_related("car")
                    .get(car__id=car.id)
                )
                provider_car_price.save(percent=percent)

            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProviderDiscountDetailView(APIView):
    permission_classes = (IsSupplierAdminOrReadOnly,)

    def get(self, request, pk):
        discount = get_object_or_404(SupplierDiscount, pk=pk, is_active=True)
        serializer = SupplierDiscountSerializer(instance=discount)
        return Response(serializer.data)

    def put(self, request, pk):
        discount = get_object_or_404(SupplierDiscount, pk=pk, is_active=True)
        serializer = SupplierDiscountSerializer(
            instance=discount, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            supplier = discount.supplier
            cars = find_cars_by_specification(discount.params)
            percent = discount.percent

            for car in cars:
                supplier_car_price = (
                    SupplierCars.objects.filter(supplier__id=supplier.id)
                    .select_related("car")
                    .get(car__id=car.id)
                )
                supplier_car_price.save(percent=percent)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        discount = get_object_or_404(SupplierDiscount, pk=pk, is_active=True)
        discount.is_active = False
        discount.save()

        supplier = discount.supplier
        cars = find_cars_by_specification(discount.params)
        for car in cars:
            try:
                supplier_car_price = (
                    SupplierCars.objects.filter(supplier__id=supplier.id)
                    .select_related("car")
                    .get(car__id=car.id)
                )
            except SupplierCars.DoesNotExist:
                supplier_car_price = None
            if supplier_car_price:
                supplier_car_price.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
