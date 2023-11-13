from django.test import TestCase
from djangoTask.src.apps.Car.models import Car
from djangoTask.src.apps.CarDealer.views import BaseViewSet
from djangoTask.src.core.factories.cars_factory import CarFactory


class BaseViewSetTest(TestCase):
    def test_perform_destroy(self):
        obj = Car.objects.create()
        view = BaseViewSet()
        view.perform_destroy(obj)
        obj.refresh_from_db()  # Update obj from db
        self.assertFalse(obj.is_active)

