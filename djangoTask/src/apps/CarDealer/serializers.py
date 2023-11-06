from rest_framework import serializers
from .models import CarDealer


class CarDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealer
        fields = '__all__'


