import datetime
import json
import os
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.utils import translation
from django.views.decorators.cache import cache_page
# from cassiopeia import Champion, Champions


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

META_DESC = "Do you love League of Legends? So do we. League Census is an information site, including champion and item rankings."


@cache_page(CACHE_TTL)
def champion_list(request):
    data = open(os.path.join(settings.BASE_DIR, 'core/static/core/ddragon/dragontail-' + get_patch() + '/' + get_patch() + '/data/en_us/champion.json')).read()
    champion_json_dump = json.loads(data)

    champion_names_images = {}
    for key in champion_json_dump['data']:
        row = champion_json_dump['data'][key]
        champion_names_images[row['name']] = row['image']['full']

    return render(request, "champion/index.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census - Champions",
        "meta_desc": META_DESC,
        "champion_names_images": champion_names_images,
        "patch": get_patch(),
    })


@cache_page(CACHE_TTL)
def champion(request, champion_name):
    champion_name = name_check(champion_name)
    data = open(os.path.join(settings.BASE_DIR, 'core/static/core/ddragon/dragontail-' + get_patch() + '/' + get_patch() + '/data/en_us/champion/' + champion_name + '.json')).read()
    champion_json_dump = json.loads(data)

    champion_data = {}
    for key, value in champion_json_dump['data'][champion_name].items():
        champion_data[key] = [value][0]

    if champion_data['partype'] == "Mana":
        resource_bg = "rgba(30, 144, 255, 1)"
        resource_color = "inherit"
    elif champion_data['partype'] == "Energy" or champion_data['partype'] == "Courage" or champion_data['partype'] == "Heat":
        resource_bg = "gold"
        resource_color = "black"
    elif champion_data['partype'] == "Fury" or champion_data['partype'] == "Rage" or champion_data['partype'] == "Crimson Rush":
        resource_bg = "rgba(218, 44, 67, 1)"
        resource_color = "inherit"
    elif champion_data['partype'] == "Shield" or champion_data['partype'] == "Flow" or champion_data['partype'] == "Ferocity":
        resource_bg = "white"
        resource_color = "black"
    else:
        resource_bg = "gray"
        resource_color = "black"

    new_stats = fix_stat_names(champion_data['stats'])

    # print(champion_data)

    return render(request, "champion/champion.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census - " + champion_name,
        "meta_desc": META_DESC,
        "champion_data": champion_data,
        "champion_name": champion_name,
        "stats": new_stats,
        "patch": get_patch(),
        "resource_bg": resource_bg,
        "resource_color": resource_color,
    })


def fix_stat_names(stats):
    new_stat_names = {
        "hp": "Hit Points",
        "hpperlevel": "Hit Points / Level",
        "mp": "Mana Points",
        "mpperlevel": "Mana Points / Level",
        "movespeed": "Move Speed",
        "armor": "Armor",
        "armorperlevel": "Armor / Level",
        "spellblock": "Magic Resist",
        "spellblockperlevel": "Magic Resist / Level",
        "attackrange": "Attack Range",
        "hpregen": "Hit Points Regen",
        "hpregenperlevel": "Hit Points Regen / Level",
        "mpregen": "Mana Points Regen",
        "mpregenperlevel": "Mana Points Regen / Level",
        "crit": "Crit Chance",
        "critperlevel": "Crit Chance / Level",
        "attackdamage": "Attack Damage",
        "attackdamageperlevel": "Attack Damage / Level",
        "attackspeedperlevel": "Attack Speed / Level",
        "attackspeed": "Attack Speed"
    }

    new_stats = dict((new_stat_names[key], value) for (key, value) in stats.items())

    return new_stats


def name_check(name):
    if name == "Cho'Gath":
        name = "Chogath"
    elif name == "Aurelion Sol":
        name = "AurelionSol"
    elif name == "Dr. Mundo":
        name = "DrMundo"
    elif name == "Jarvan IV":
        name = "JarvanIV"
    elif name == "Kha'Zix":
        name = "Khazix"
    elif name == "Kog'Maw":
        name = "KogMaw"
    elif name == "Lee Sin":
        name = "LeeSin"
    elif name == "Master Yi":
        name = "MasterYi"
    elif name == "Miss Fortune":
        name = "MissFortune"
    elif name == "Nunu & Willump":
        name = "Nunu"
    elif name == "Rek'Sai":
        name = "RekSai"
    elif name == "Tahm Kench":
        name = "TahmKench"
    elif name == "Twisted Fate":
        name = "TwistedFate"
    elif name == "Vel'Koz":
        name = "Velkoz"
    elif name == "Xin Zhao":
        name = "XinZhao"
    elif name == "Wukong":
        name = "MonkeyKing"  # Wukong/MonkeyKing

    return name


def get_year():
    return datetime.datetime.now().year


def get_language():
    return translation.get_language()


def get_patch():
    return settings.PATCH_VERSION
