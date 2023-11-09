from django_countries.fields import CountryField
from rest_framework import serializers
from .models import CarDealer
from djangoTask.src.apps.Car.serializers import CarSerializer, SpecificationCarSerializer


class CarDealerSerializer(serializers.ModelSerializer):
    car_price = serializers.SerializerMethodField()
    car_price_with_discount = serializers.SerializerMethodField()
    count_of_car = serializers.SerializerMethodField()
    country = CountryField()
    cars = CarSerializer(many=True, required=False)
    specification = SpecificationCarSerializer(many=True, required=False)

    class Meta:
        model = CarDealer
        fields = [
            "id",
            "dealer_name",
            "country",
            "balance",
            "cars",
            "specification",
            "car_price",
            "car_price_with_discount",
            "count_of_car"
        ]
        read_only_fields = {
            'balance',
            'cars'
        }
