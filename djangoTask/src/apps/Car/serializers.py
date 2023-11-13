import datetime

from django.core.validators import MinValueValidator
from rest_framework import serializers
from djangoTask.src.apps.Car.models import Car
from djangoTask.src.core.enums.enums import Color


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class SpecificationCarSerializer(serializers.Serializer):  # Specification for Cars: we serialize data from JSON
    max_price = serializers.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    brand = serializers.CharField(max_length=20, default=None)
    model = serializers.CharField(max_length=20, default=None)
    year = serializers.IntegerField(default=2023)
    color = serializers.ChoiceField(
        choices=Color.choices, default=Color.WHITE.value
    )
