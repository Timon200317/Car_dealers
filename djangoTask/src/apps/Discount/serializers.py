from datetime import date

from rest_framework import serializers
from .models import SupplierDiscount, CarDealerDiscount


class SupplierDiscountSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if date.today() <= data["date_start"] <= data["date_end"]:
            return data
        else:
            raise serializers.ValidationError(
                {"end_date": "end date should be greater that start date"}
            )

    class Meta:
        model = SupplierDiscount
        fields = '__all__'


class CarDealerDiscountSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if date.today() <= data["date_start"] <= data["date_end"]:
            return data
        else:
            raise serializers.ValidationError(
                {"end_date": "end date should be greater that start date"}
            )

    class Meta:
        model = CarDealerDiscount
        fields = '__all__'
