from rest_framework import serializers
from .models import CarDealer


class CarDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealer
        fields = '__all__'
        extra_kwargs = {
            'balance': {'read_only': True},
        }
