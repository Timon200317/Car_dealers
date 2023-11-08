from rest_framework import serializers
from .models import SupplierPromotion, CarDealerPromotion


class SupplierPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierPromotion
        fields = '__all__'


class CarDealerPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealerPromotion
        fields = '__all__'
