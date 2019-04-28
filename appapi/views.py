from django.shortcuts import render, redirect
import requests
import secret


# Create your views here.
def weather_view(request):

    return render(request, "appapi/weather.html")


def visa_view(request):
    cs = request.POST.get("citizenship")
    d = request.POST.get("destination")
    lan = "en"
    path = f"https://requirements-api.sandbox.joinsherpa.com/v2/entry-requirements?citizenship=" \
        f"{cs}&destination={d}&language={lan}&key={secret.SHERPA_API}"
    download = requests.get(path).json()
    for k, v in download.items():
        print(v)
    return render(request, "appapi/visa.html")
