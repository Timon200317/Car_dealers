from django.db import IntegrityError
from django.db.models import Sum, F
from django_countries.fields import CountryField
from rest_framework import serializers
from .models import Client
from djangoTask.src.apps.Car.serializers import SpecificationCarSerializer
from ..History.models import SalesDealerHistory
from ..User.models import User
from ..User.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    specification = SpecificationCarSerializer(many=True, required=False)
    exclude = ["is_active", "id", "user", "balance"]

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ["balance", "client_name",
                            "client_second_name", ]
        depth = 1


class ClientCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    client_name = serializers.CharField()
    client_second_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    specification = serializers.JSONField()

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        client_name = validated_data.get('client_name')
        client_second_name = validated_data.get('client_second_name')
        phone_number = validated_data.pop('phone_number')
        email = validated_data.pop('email')
        specification = validated_data.pop('specification')
        try:
            client = Client.objects.create(
                user_id=user_id,
                client_name=client_name,
                client_second_name=client_second_name,
                phone_number=phone_number,
                email=email,
                specification=specification,
            )
            return client
        except IntegrityError:
            raise serializers.ValidationError("This car already exists in this car dealer")


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
