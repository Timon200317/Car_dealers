import datetime

from django.core.validators import MinValueValidator
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
            .values_list("supplier__name", flat=True)
            .distinct()
        )

    class Meta:
        model = CarDealer
        fields = ("unique_suppliers",)
