from django.db.models import Sum, F
from django_countries.fields import CountryField
from psycopg2 import IntegrityError
from rest_framework import serializers
from .models import CarDealer
from djangoTask.src.apps.Car.serializers import CarSerializer, SpecificationCarSerializer
from ..Car.models import CarDealerCar
from ..History.models import SalesDealerHistory, SupplierSalesHistory


class CarDealerCarsSerializer(serializers.Serializer):
    car_id = serializers.IntegerField()
    count = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=12, decimal_places=2)

    def create(self, validated_data):
        car_id = validated_data.get('car_id')
        count = validated_data.get('count')
        price = validated_data.get('price')

        try:
            car_dealer_car = CarDealerCar.objects.create(
                car_id=car_id,
                car_dealer=self.context['car_dealer'],
                count=count,
                price=price
            )
            return car_dealer_car
        except IntegrityError:
            raise serializers.ValidationError("This car already exists in this car dealer")


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


class CarDealerUniqueClientsSerializer(serializers.ModelSerializer):
    unique_clients = serializers.SerializerMethodField()

    def get_unique_clients(self, *args, **kwargs):
        return (
            SalesDealerHistory.objects.filter(is_active=True, car_dealer=self.context["car_dealer_id"])
            .values("car_dealer")
            .values_list("client__user__username", flat=True)
            .distinct()
        )

    class Meta:
        model = CarDealer
        fields = ("unique_clients",)


class CarDealerUniqueSuppliersSerializer(serializers.ModelSerializer):
    unique_suppliers = serializers.SerializerMethodField()

    def get_unique_suppliers(self, *args, **kwargs):
        return (
            SupplierSalesHistory.objects.filter(is_active=True, car_dealer=self.context["car_dealer_id"])
            .values("car_dealer")
            .values_list("supplier__supplier_name", flat=True)
            .distinct()
        )

    class Meta:
        model = CarDealer
        fields = ("unique_suppliers",)


class CarDealerNumberOfSellsSerializer(serializers.ModelSerializer):
    number_of_sells = serializers.SerializerMethodField()

    def get_number_of_sells(self, *args, **kwargs):
        return (
            SalesDealerHistory.objects.filter(is_active=True, car_dealer=self.context["car_dealer_id"])
            .values("car_dealer")
            .annotate(Sum("count"))
            .values_list("count__sum", flat=True)[0]
        )

    class Meta:
        model = CarDealer
        fields = ("number_of_sells",)


class CarDealerProfitSerializer(serializers.ModelSerializer):
    profit = serializers.SerializerMethodField()

    def get_profit(self, *args, **kwargs):
        return (
            SalesDealerHistory.objects.filter(is_active=True, car_dealer=self.context["car_dealer_id"])
            .values("car_dealer")
            .annotate(profit_sum=Sum(F("count") * F("price")))
            .values_list("profit_sum", flat=True)[0]
        )

    class Meta:
        model = CarDealer
        fields = ("profit",)
