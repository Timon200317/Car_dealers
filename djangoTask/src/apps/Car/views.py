from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CarSerializer
from .models import Car
from djangoTask.src.core.tools.permissions import IsSupplierAdminOrReadOnly


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)


