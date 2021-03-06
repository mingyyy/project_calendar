from django.shortcuts import render, redirect
import requests
import secret
from .forms import EntryRequirementForm
from django.contrib import messages


def visa_view(request):
    form = EntryRequirementForm(request.GET or None)
    # default requirement = Unkown, citizenship is US, destination is Vietnam
    lan = "en"
    cs = "US"
    d = "VN"
    requirement, portrestriction, allowedstay, type = "Unknown", "Unknown", "Unknown", "Unknown"
    passport_validity, password_blank_pages = "Unknown", "Unknown"
    country_name, country_call_code, country_capital, country_timezone, country_population = \
        "Unknown", "Unknown", "Unknown","Unknown","Unknown"
    weather_temp,weather_temp_min,weather_temp_max, weather_humidity="Unknown", "Unknown", "Unknown", "Unknown"
    ccy_arrival, ccy_exit = "Unknown","Unknown"
    textual=[]
    if request.GET:
        cs = request.GET["citizenship"]
        d = request.GET["destination"]
        # messages.success(request, f"You are from {cs} and going to visit {d}.")
    else:
        form=EntryRequirementForm()
    if cs == d:
        requirement = "NOT_REQUIRED"
        portrestriction = "None"
        allowedstay = "Unlimited"
        type = "Citizenship"
        passport_validity, password_blank_pages = "None", "None"
        ccy_arrival, ccy_exit = "Unlimited", "Unlimited"
        textual = ["Probably you don't need a visa to visit your country."]
    else:
        url = "https://requirements-api.sandbox.joinsherpa.com/v2/entry-requirements"
        querystring = {"citizenship": cs, "destination": d, "language": lan,
                       "key": secret.SHERPA_API}
        headers = {'accept': '*/*'}
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            visa_info=response.json()
            for k, v in visa_info.items():
                if k == "visa":
                    for key, value in v[0].items():
                        print(key)
                        if key == "requirement":
                            requirement = value
                        elif key == "allowedStay":
                            allowedstay= value
                        elif key == "portRestriction":
                            portrestriction = value
                        elif key == "type":
                            type = value
                        elif key == "textual":
                            for x in value["text"]:
                                textual.append(x)
                if k == "passport":
                    passport_validity = v["passport_validity"]
                    password_blank_pages = v["blank_pages"]
                if k == "currency":
                    ccy_exit = v["exit"]
                    ccy_arrival = v["arrival"]
                # if k == "vaccination":
        except:
            messages.warning(request, "Sorry, visa requirement to this country is not available at the moment.")

    try:
        country_info = requests.get(f"https://restcountries.eu/rest/v2/alpha/{d}").json()
        for k, v in country_info.items():
            if k == "name":
                country_name = v
            elif k == "callingCodes":
                country_call_code = v[0]
            elif k == "capital":
                country_capital = v
            elif k == "population":
                country_population = v
            elif k == "timezones":
                country_timezone = v[0]
    except:
        messages.warning(request, "Sorry, there is no info for this country.")
    weather_desc=[]

    try:
        path = f"https://api.openweathermap.org/data/2.5/weather?q={country_capital}&units=metric&appid={secret.OPEN_WEATHER_API}"
        print(path)
        weather_info = requests.get(path).json()
        print(path)
        for k, v in weather_info.items():
            if k == "weather":
                for x in v:
                    weather_desc.append(x["main"])
            if k == "main":
                weather_temp = v["temp"]
                weather_temp_min = v["temp_min"]
                weather_temp_max = v["temp_max"]
                weather_humidity = v["humidity"]
    except:
        messages.warning(request, "Sorry, there is no weather info for this city.")

    context = {"form": form, "requirement": requirement, "allowedstay": allowedstay,
               "portrestriction": portrestriction,"type": type, "textual": textual,
               "country_name": country_name, "country_call_code": country_call_code,
               "country_capital": country_capital, "country_population": country_population,
               "country_timezone": country_timezone, "passport_validity": passport_validity,
               "passport_blank_pages": password_blank_pages,"currency_exit": ccy_exit,
               "currency_arrival": ccy_arrival, "weather_desc": weather_desc, "weather_temp": weather_temp,
               "weather_temp_min": weather_temp_min, "weather_temp_max": weather_temp_max,
               "weather_humidity": weather_humidity}
    return render(request, "appapi/visa.html", context)


# def cities_view(request):
#     input_address = ''
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             input_address = form.cleaned_data['address']
#     else:
#         form = PersonForm()
#     context = {form:'form', 'input_address':'input_address'}
#     return render(request, "appapi/cities.html", context)
