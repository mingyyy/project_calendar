from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from .forms import FormCountry, FormCity
import json, os
from social_django.models import UserSocialAuth
from pjcalendar.settings import BASE_DIR


def home(request):
    chosen_country = ''
    chosen_city = ''
    if request.method == 'POST':
        form = FormCountry(request.POST)
        if form.is_valid():
            x=form.cleaned_data['country']
            chosen_country = x[0]

            form_city = FormCity(request.POST, country=chosen_country)
            if form_city.is_valid():
                chosen_city = form_city.cleaned_data['city']
        else:
            form_city=FormCity(country='Canada')
    else:
        form = FormCountry()
        form_city = FormCity(country='Canada')
    context = {'form': form, 'form_city': form_city, "chosen_country": chosen_country, "chosen_city": chosen_city}
    return render(request, 'appmain/home.html',context )


@login_required
def dashboard_view(request):
    return render(request, 'appmain/dashboard.html')

@login_required
def settings_view(request):
    user = request.user
    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None
    can_disconnect = (user.social_auth.count()>1 or user.has_usable_password())
    context = {'github': github_login, 'twitter_login': twitter_login,
               'facebook_login': facebook_login, 'can_disconnect': can_disconnect}
    return render(request, 'appmain/settings.html',context)


@login_required
def password_view(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == "POST":
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        form = PasswordForm(request.user)
    return render(request, 'appmain/password.html', {'form': form})
