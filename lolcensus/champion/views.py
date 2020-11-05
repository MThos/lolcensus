import datetime
import json
import os
from cassiopeia import Champion, Champions
from django.utils import translation
from django.shortcuts import render
from django.conf import settings


def champion_list(request):
    year = datetime.datetime.now().year
    get_current_lang = translation.get_language()
    data = open(os.path.join(settings.BASE_DIR,  'champion/static/champion/ddragon/dragontail-10.2.1/10.2.1/data/en_us/champion.json')).read()
    champion_data = json.loads(data)
    champion_dict = {}
    for key in champion_data['data']:
        row = champion_data['data'][key]
        champion_dict[row['name']] = row['image']['full']

    return render(request, "champion/index.html", {
        "year": year,
        "get_current_language": get_current_lang,
        "tab_title": "League Census",
        "champion_dict": champion_dict,
    })


def champion(request, champion_name):
    year = datetime.datetime.now().year
    get_current_lang = translation.get_language()
    data = open(os.path.join(settings.BASE_DIR,  'champion/static/champion/ddragon/dragontail-10.2.1/10.2.1/data/en_us/champion/' + champion_name + '.json')).read()
    json_dump = json.loads(data)
    champion_data = {}
    for key, value in json_dump['data'][champion_name].items():
        champion_data[key] = [value][0]

    patch = json_dump['version']
    print(champion_data)

    return render(request, "champion/champion.html", {
        "year": year,
        "get_current_language": get_current_lang,
        "tab_title": "League Census",
        "champion_data": champion_data,
        "patch": patch
    })
