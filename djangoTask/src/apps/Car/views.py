from rest_framework import viewsets
from .serializers import BrandSerializer, ModelSerializer, CarSerializer
from .models import Model, Brand, Car
from djangoTask.src.core.tools.permissions import IsSupplierAdminOrReadOnly


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = (IsSupplierAdminOrReadOnly,)
