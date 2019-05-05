from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from .forms import FormCountry
import json, os
from social_django.models import UserSocialAuth
from pjcalendar.settings import BASE_DIR


def home(request):
    filepath = os.path.join(BASE_DIR, "appmain/static/appmain/countries.min.json")
    with open(filepath, "r") as f:
        country_file = json.load(f)
    country_list=[]
    for k, v in country_file.items():
        country_list.append(k)


    # if request.method == "GET":
    #     form_country = request.GET["country"]
    # else:
    #     form_country = FormCountry()
    # context = {"country_city":country_file, "form_country":form_country}
    context = {"country_list": country_list}
    return render(request, 'appmain/home.html', context)

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
