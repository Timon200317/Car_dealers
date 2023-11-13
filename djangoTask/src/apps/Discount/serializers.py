from rest_framework import serializers
from .models import SupplierDiscount, CarDealerDiscount


class SupplierDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierDiscount
        fields = '__all__'


class CarDealerDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealerDiscount
        fields = '__all__'
