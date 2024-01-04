import datetime

from django.core.validators import MinValueValidator
from django.db.models import Count, Sum, F
from rest_framework import serializers
from djangoTask.src.apps.Car.models import Car
from djangoTask.src.apps.CarDealer.models import CarDealer
from djangoTask.src.apps.History.models import SupplierSalesHistory, SalesDealerHistory
from djangoTask.src.core.enums.enums import Color


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class SpecificationCarSerializer(serializers.Serializer):
    max_price = serializers.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    brand = serializers.CharField(max_length=20, default=None)
    model = serializers.CharField(max_length=20, default=None)
    color = serializers.ChoiceField(
        choices=Color.choices, default=Color.WHITE.value
    )


class CarDealerUniqueClientsSerializer(serializers.ModelSerializer):
    unique_clients = serializers.SerializerMethodField()

    def get_unique_clients(self, *args, **kwargs):
        return (
            SalesDealerHistory.objects.filter(car_dealer=self.context["car_dealer_id"])
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
            SupplierSalesHistory.objects.filter(car_dealer=self.context["car_dealer_id"])
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
            SalesDealerHistory.objects.filter(car_dealer=self.context["car_dealer_id"])
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
            SalesDealerHistory.objects.filter(car_dealer=self.context["car_dealer_id"])
            .values("car_dealer")
            .annotate(profit_sum=Sum(F("count") * F("price")))
            .values_list("profit_sum", flat=True)[0]
        )

    class Meta:
        model = CarDealer
        fields = ("profit",)

