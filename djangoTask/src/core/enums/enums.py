from enum import Enum


class Color(Enum):  # Colors for cars
    RED = 'Red'
    BLUE = 'Blue'
    GREEN = 'Green'
    YELLOW = 'Yellow'
    WHITE = 'White'
    BLACK = 'Black'
    SILVER = 'Silver'
    GRAY = 'Gray'


class UserProfile(Enum):  # User Type
    NONE = "none"
    CLIENT = "client"
    CAR_DEALER = "car_dealer"
    SUPPLIER = "supplier"
