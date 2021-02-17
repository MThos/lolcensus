import datetime
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import  HttpResponse, HttpResponseRedirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render, redirect
from django.utils import translation
from django.views.decorators.cache import cache_page
from ..forms import ContactForm

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

META_DESC = "Do you love League of Legends? So do we. League Census is an information site, including champion and item rankings."


@cache_page(CACHE_TTL)
def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@leaguecensus.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            return redirect('success')
    return render(request, "core/contact.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census - Contact Us",
        "meta_desc": META_DESC,
        "form": form,
    })


@cache_page(CACHE_TTL)
def terms(request):
    return render(request, "core/terms.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census - Terms of Service",
        "meta_desc": META_DESC,
    })


@cache_page(CACHE_TTL)
def privacy(request):
    return render(request, "core/privacy.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census - Privacy Policy",
        "meta_desc": META_DESC,
    })


@cache_page(CACHE_TTL)
def cookies(request):
    return render(request, "core/cookies.html", {
        "year": get_year(),
        "get_current_language": get_language(),
        "tab_title": "League Census - Cookies Policy",
        "meta_desc": META_DESC,
    })


def get_year():
    return datetime.datetime.now().year


def get_language():
    return translation.get_language()
