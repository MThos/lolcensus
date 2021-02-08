import datetime
import requests
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.utils import translation
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def terms(request):
    return render(request, "core/terms.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census",
    })


@cache_page(CACHE_TTL)
def privacy(request):
    return render(request, "core/privacy.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census",
    })


@cache_page(CACHE_TTL)
def cookies(request):
    return render(request, "core/cookies.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census",
    })


@cache_page(CACHE_TTL)
def status(request):
    server_status = requests.get("https://na1.api.riotgames.com/lol/status/v4/platform-data?api_key=" + settings.API_KEY)
    print(server_status.json())
    return render(request, "core/status.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census",
    })


def get_year():
    return datetime.datetime.now().year


def get_language():
    return translation.get_language()
