from django.db import models
from djangoTask.src.core.models.abstract_models import Base
from django_countries.fields import CountryField


class Supplier(Base):
    supplier_name = models.CharField(max_length=255)
    year_of_origin = models.PositiveIntegerField()
    country = CountryField()

    def __str__(self):
        return self.supplier_name

    class Meta:
        ordering = ['supplier_name']
