from django.test import TestCase
from djangoTask.src.apps.Car.models import Brand
from djangoTask.src.apps.CarDealer.views import BaseViewSet


class BaseViewSetTest(TestCase):
    def test_perform_destroy(self):
        obj = Brand.objects.create()
        view = BaseViewSet()
        view.perform_destroy(obj)
        obj.refresh_from_db()  # Update obj from db
        self.assertFalse(obj.is_active)

