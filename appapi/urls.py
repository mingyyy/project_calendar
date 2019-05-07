from django.urls import path
from .views import visa_view

app_name = "appapi"

urlpatterns = [
    # path('cities/', cities_view, name="cities"),
    path('visa/', visa_view, name="visa"),
]