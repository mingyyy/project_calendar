from django.urls import path
from .views import home

app_name = "appmain"

urlpatterns = [
    path('', home, name="home"),
]