from django.db import models
from djangoTask.src.core.models.abstract_models import Base
from djangoTask.src.apps.User.models import User
from django_countries.fields import CountryField


class Supplier(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255, unique=True)
    year_of_origin = models.PositiveIntegerField()
    country = CountryField()

    def __str__(self):
        return self.supplier_name

    class Meta:
        ordering = ['supplier_name']
