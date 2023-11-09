from django.db import models


class Color(models.TextChoices):  # Colors for cars
    RED = 'Red'
    BLUE = 'Blue'
    GREEN = 'Green'
    YELLOW = 'Yellow'
    WHITE = 'White'
    BLACK = 'Black'
    SILVER = 'Silver'
    GRAY = 'Gray'


class UserProfile(models.TextChoices):  # User Type
    NONE = "none"
    CLIENT = "client"
    CAR_DEALER = "car_dealer"
    SUPPLIER = "supplier"
