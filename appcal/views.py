from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def cal1_view(request):
    return render(request, "appcal/cal1.html")
