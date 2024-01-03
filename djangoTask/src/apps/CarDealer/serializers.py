from django_countries.fields import CountryField
from rest_framework import serializers
from .models import CarDealer
from djangoTask.src.apps.Car.serializers import CarSerializer, SpecificationCarSerializer


class CarDealerSerializer(serializers.ModelSerializer):
    car_price = serializers.SerializerMethodField()
    car_price_with_discount = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    country = CountryField()
    cars = CarSerializer(many=True, required=False)
    specification = SpecificationCarSerializer(many=True, required=False)

    def get_car_price(self, obj):
        supplier_cars = obj.cardealercar_set.all()
        return {car.car_id: car.price for car in supplier_cars}

    def get_car_price_with_discount(self, obj):
        car_dealer_cars = obj.cardealercar_set.all()
        return {car.car_id: car.price_with_discount for car in car_dealer_cars}

    def get_count(self, obj):
        car_dealer_cars = obj.cardealercar_set.all()
        return {car.car_id: car.count for car in car_dealer_cars}

    class Meta:
        model = CarDealer
        fields = [
            "id",
            "dealer_name",
            "country",
            "balance",
            "cars",
            "car_price",
            "car_price_with_discount",
            "count",
            "specification"
        ]

        depth = 1
