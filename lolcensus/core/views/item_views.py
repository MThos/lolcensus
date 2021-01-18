import datetime
import json
import os
from django.utils import translation
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from collections import OrderedDict

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def item_list(request):
    data = open(os.path.join(settings.BASE_DIR, 'core/static/core/ddragon/dragontail-' + get_patch() + '/' + get_patch() + '/data/en_us/item.json')).read()
    item_json_dump = json.loads(data)

    item_names_images_unsort = {}
    for key in item_json_dump['data']:
        row = item_json_dump['data'][key]
        item_names_images_unsort[row['name']] = row['image']['full']

    item_names_images = OrderedDict(sorted(item_names_images_unsort.items()))

    return render(request, "item/index.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census",
        "item_names_images": item_names_images,
        "patch": get_patch(),
    })


@cache_page(CACHE_TTL)
def item(request, item_id):
    data = open(os.path.join(settings.BASE_DIR, 'core/static/core/ddragon/dragontail-' + get_patch() + '/' + get_patch() + '/data/en_us/item.json')).read()
    item_json_dump = json.loads(data)

    item_data = {}
    for key, value in item_json_dump['data'][item_id].items():
        item_data[key] = [value][0]

    map_data = {'mapName': []}
    for key, value in item_json_dump['data'][item_id]['maps'].items():
        if value:
            map_data['mapName'].append(get_map_details(key))

    return render(request, "item/item.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census",
        "item_data": item_data,
        "map_data": map_data,
        "item_id": item_id,
        "patch": get_patch(),
    })


def get_map_details(map_id):
    data = open(os.path.join(settings.BASE_DIR, 'core/static/core/json/maps.json')).read()
    map_json_dump = json.loads(data)

    for maps in map_json_dump:
        if maps["mapId"] == int(map_id):
            return maps["mapName"]


def get_year():
    return datetime.datetime.now().year


def get_language():
    return translation.get_language()


def get_patch():
    return settings.PATCH_VERSION
