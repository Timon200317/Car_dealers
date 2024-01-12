from django.db import IntegrityError
from django.db.models import Sum, F
from django_countries.fields import CountryField
from rest_framework import serializers
from .models import Supplier, SupplierCars
from ..Car.serializers import CarSerializer
from ..History.models import SupplierSalesHistory


class SupplierCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    supplier_name = serializers.CharField()
    year_of_origin = serializers.CharField()
    country = CountryField()

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        supplier_name = validated_data.get('supplier_name')
        year_of_origin = validated_data.get('year_of_origin')
        country = validated_data.get('country')
        try:
            supplier = Supplier.objects.create(
                user_id=user_id,
                supplier_name=supplier_name,
                year_of_origin=year_of_origin,
                country=country,
            )
            return supplier
        except IntegrityError:
            raise serializers.ValidationError("This supplier already exists")


class SupplierSerializer(serializers.ModelSerializer):
    country = CountryField()
    cars = CarSerializer(many=True, required=False)

    class Meta:
        model = Supplier
        fields = [
            "supplier_name",
            "year_of_origin",
            "cars",
        ]
        read_only_fields = [
            "cars",
        ]


class SupplierCarsSerializer(serializers.Serializer):
    car_id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=12, decimal_places=2)

    def create(self, validated_data):
        car_id = validated_data.get('car_id')
        price = validated_data.get('price')

        try:
            supplier_car = SupplierCars.objects.create(
                car_id=car_id,
                supplier=self.context['supplier'],
                price=price
            )
            return supplier_car
        except IntegrityError:
            raise serializers.ValidationError("This car already exists in this supplier")


class SupplierUniqueCarDealersSerializer(serializers.ModelSerializer):
    unique_car_dealers = serializers.SerializerMethodField()

    def get_unique_car_dealers(self, *args, **kwargs):
        return (
            SupplierSalesHistory.objects.filter(is_active=True, car_dealer=self.context["supplier_id"])
            .values("supplier")
            .values_list("car_dealer__user__username", flat=True)
            .distinct()
        )

    class Meta:
        model = Supplier
        fields = ("unique_car_dealers",)


class SupplierProfitSerializer(serializers.ModelSerializer):
    profit_supplier = serializers.SerializerMethodField()

    def get_profit_supplier(self, *args, **kwargs):
        return (
            SupplierSalesHistory.objects.filter(is_active=True, car_dealer=self.context["supplier_id"])
            .values("supplier")
            .annotate(profit_sum=Sum(F("count") * F("price")))
            .values_list("profit_sum", flat=True)[0]
        )

    class Meta:
        model = Supplier
        fields = ("profit_supplier",)
