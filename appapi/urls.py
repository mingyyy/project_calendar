from django.urls import path
from .views import weather_view, visa_view

app_name = "appapi"

urlpatterns = [
    path('weather/', weather_view, name="weather"),
    path('visa/', visa_view, name="visa"),
]