from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/driver/register/', views.driver, name='register'),
    path('api/v1/driver/<int:id>/sendLocation/', views.driverLocation, name='driver_location'),
    path('api/v1/passenger/available_cabs/', views.passengers, name="cabsearch")
]