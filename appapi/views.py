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
    country_name, country_call_code, country_capital, country_timezone, country_population = \
        "Unknown", "Unknown", "Unknown","Unknown","Unknown"
    textual=[]
    if request.GET:
        cs = request.GET["citizenship"]
        d = request.GET["destination"]
        messages.success(request, f"You are from {cs} and going to visit {d}.")
    else:
        form=EntryRequirementForm()
    url = "https://requirements-api.sandbox.joinsherpa.com/v2/entry-requirements"
    querystring = {"citizenship": cs, "destination": d, "language": lan,
                   "key": secret.SHERPA_API}
    headers = {'accept': '*/*'}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        visa_info=response.json()
        print(visa_info)
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
    except:
        messages.warning(request, "Sorry, visa requirement to this country is not available at the moment.")

    try:
        country_info = requests.get(f"https://restcountries.eu/rest/v2/alpha/{d}").json()
        for k, v in country_info.items():
            if k == "name":
                country_name = v
            elif k == "callingCodes":
                country_call_code = v
            elif k == "capital":
                country_capital = v
            elif k == "population":
                country_population = v
            elif k == "timezones":
                country_timezone = v

    except:
        messages.warning(request, "Sorry, there is no info for this country.")

    context = {"form": form, "requirement": requirement, "allowedstay": allowedstay,
               "portrestriction":portrestriction,"type": type, "textual": textual,
               "country_name": country_name, "country_call_code": country_call_code,
               "country_capital":country_capital, "country_population":country_population,
               "country_timezone": country_timezone}
    return render(request, "appapi/visa.html", context)


def weather_view(request):

    return render(request, "appapi/weather.html")
