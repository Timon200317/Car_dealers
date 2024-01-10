from rest_framework import serializers
from .models import BaseHistory, SalesDealerHistory, SupplierSalesHistory


class BaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseHistory
        fields = '__all__'


class SalesDealerHistorySerializer(BaseHistorySerializer):
    class Meta:
        model = SalesDealerHistory
        fields = '__all__'


class SupplierSalesHistorySerializer(BaseHistorySerializer):
    class Meta:
        model = SupplierSalesHistory
        fields = '__all__'
