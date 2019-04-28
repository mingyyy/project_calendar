"""pjcalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from appmain.views import dashboard_view,settings_view, password_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(template_name='appuser/login.html'),name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('oauth/',include('social_django.urls',namespace='social')),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('settings/', settings_view, name='settings'),
    path('password/', password_view, name='password'),
    path('', include('appmain.urls')),
    path('',include('appapi.urls')),
    # path('fb/', fb_view, name='fb')
    # path('user/',include('appuser.urls')),
]

