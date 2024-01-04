from django.db.models import Sum, F
from django_countries.fields import CountryField
from rest_framework import serializers
from .models import Supplier
from ..Car.serializers import CarSerializer
from ..History.models import SupplierSalesHistory


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    country = CountryField()
    cars = CarSerializer(many=True, required=False)
    car_price = serializers.SerializerMethodField()
    car_price_with_discount = serializers.SerializerMethodField()

    def get_car_price(self, obj):
        supplier_cars = obj.supplier_cars_set.all()
        return {car.car_id: car.price for car in supplier_cars}

    def get_car_price_with_discount(self, obj):
        car_dealer_cars = obj.supplier_cars_set.all()
        return {car.car_id: car.price_with_discount for car in car_dealer_cars}

    class Meta:
        model = Supplier
        fields = [
            "supplier_name",
            "year_of_origin",
            "cars",
            "country",
            "car_price",
            "car_price_with_discount",
            "user",
        ]
        read_only_fields = [
            "cars",
        ]
        depth = 1


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
