from rest_framework import viewsets, permissions
from rest_framework.exceptions import APIException

from .serializers import CarDealerSerializer
from .models import CarDealer


class CarDealerViewSet(viewsets.ModelViewSet):
    queryset = CarDealer.objects.all()
    serializer_class = CarDealerSerializer
    permission_classes = [permissions.IsAdminUser]  # Balance field cannot be changed by simple user

    def perform_update(self, serializer):
        # Перед сохранением проверяем, что 'balance' не пытается измениться
        if 'balance' in serializer.validated_data:
            raise APIException(detail="Изменение 'balance' запрещено.", code=400)
        serializer.save()

