from django.urls import path
from .views import cal1_view

app_name = "appcal"

urlpatterns = [
    path('cal1/', cal1_view, name="cal1"),
]