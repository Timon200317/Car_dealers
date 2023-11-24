from django.urls import path, include

urlpatterns = [
    path('car_dealers/', include("djangoTask.src.apps.CarDealer.urls")),
    path('cars/', include("djangoTask.src.apps.Car.urls")),
    path('clients/', include("djangoTask.src.apps.Client.urls")),
    path('users/', include("djangoTask.src.apps.User.urls")),
    path('suppliers/', include("djangoTask.src.apps.Supplier.urls")),
]

