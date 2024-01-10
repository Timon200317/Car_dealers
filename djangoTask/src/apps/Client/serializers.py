from django.db.models import Sum, F
from django_countries.fields import CountryField
from rest_framework import serializers
from .models import Client
from djangoTask.src.apps.Car.serializers import SpecificationCarSerializer
from ..History.models import SalesDealerHistory


class ClientSerializer(serializers.ModelSerializer):
    specification = SpecificationCarSerializer(many=True, required=False)

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ["balance"]


class ClientTotalAmountSpentSerializer(serializers.ModelSerializer):
    total_client_spent = serializers.SerializerMethodField()

    def get_total_client_spent(self, *args, **kwargs):
        return (
            SalesDealerHistory.objects.filter(is_active=True, client=self.context["client_id"])
            .values("client")
            .annotate(total_spent_sum=Sum(F("count") * F("price")))
            .values_list("total_spent_sum")[0]
        )

    class Meta:
        model = Client
        fields = ("total_client_spent",)


class ClientCarsListSerializer(serializers.ModelSerializer):
    cars_number = serializers.SerializerMethodField()
    bought_cars = serializers.SerializerMethodField()

    def get_cars_number(self, *args, **kwargs):
        return (
            SalesDealerHistory.objects.filter(
                is_active=True, client__id=self.context["client_id"]
            ).aggregate(total=Sum("count"))
        )

    def get_bought_cars(self, *args, **kwargs):
        return (
            SalesDealerHistory.objects.filter(
                is_active=True, client__id=self.context["client_id"]
            )
            .annotate(sum=Sum("count"))
            .order_by("-sum")
            .values_list("car_id__brand", "car_id__model", "car_id__year", "car_id__color", "sum")
        )

    class Meta:
        model = Client
        fields = ["cars_number", "bought_cars"]
