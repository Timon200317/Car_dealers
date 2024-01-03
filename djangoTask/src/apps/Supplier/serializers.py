from django_countries.fields import CountryField
from rest_framework import serializers
from .models import Supplier
from ..Car.serializers import CarSerializer


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
