from django import forms
from ktag.fields import TagField
import os,json
from pjcalendar.settings import BASE_DIR
from copy import deepcopy

filepath = os.path.join(BASE_DIR, "appmain/static/appmain/countries.min.json")
with open(filepath, "r") as f:
    country_file = json.load(f)
CF = country_file


def get_country_list(CF):
    country_list = []
    for k, v in CF.items():
        country_list.append(k)
    country_list.sort(reverse=True)
    return country_list


def get_city_list(CF, country):
    city_list = []
    for k, v in CF.items():
        if k == country:
            city_list=v
    city_list.sort(reverse=True)
    return city_list


class FormCountry(forms.Form):
    country = TagField(label='Country:', place_holder='write the name of the country', delimiters=',',
                          data_list=get_country_list(CF), initial='Canada', max_tags=1,
                       help_text="Only one is allowed for the city list.")



class FormCity(forms.Form):
    def __init__(self, *args, **kwargs):
        self.country = kwargs.pop('country')
        super(FormCity, self).__init__(*args, **kwargs)
        self.fields['city'] = TagField(label='Choose from the city list:', place_holder='write the name of the cities', delimiters=',',
                  initial='Toronto, Ottawa', data_list=get_city_list(CF, self.country), help_text="Not more than 5 cities are allowed")

    city = TagField(label='Choose from the city list:', place_holder='write the name of the cities', delimiters=',',max_tags=5,
                initial='Toronto, Ottawa')





