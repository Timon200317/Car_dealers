from django_countries.fields import CountryField
from rest_framework import serializers
from .models import Client
from djangoTask.src.apps.Car.serializers import SpecificationCarSerializer


class ClientSerializer(serializers.ModelSerializer):
    specification = SpecificationCarSerializer(many=True, required=False)

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ["balance"]
