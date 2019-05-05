import django.forms as form


class FormCountry(form.Form):
    country = form.TextInput()
