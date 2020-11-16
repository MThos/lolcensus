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
    champion_name = name_check(champion_name)
    year = datetime.datetime.now().year
    get_current_lang = translation.get_language()
    data = open(os.path.join(settings.BASE_DIR,  'champion/static/champion/ddragon/dragontail-10.2.1/10.2.1/data/en_us/champion/' + champion_name + '.json')).read()
    json_dump = json.loads(data)

    champion_data = {}
    for key, value in json_dump['data'][champion_name].items():
        champion_data[key] = [value][0]

    patch = json_dump['version']

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
        "year": year,
        "get_current_language": get_current_lang,
        "tab_title": "League Census",
        "champion_data": champion_data,
        "champion_name": champion_name,
        "stats": new_stats,
        "patch": patch,
        "resource_bg": resource_bg,
        "resource_color": resource_color
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
