from django import template
import re

register = template.Library()


@register.filter
def slash_to_breakline(value):
    return value.replace("/", " /<br>")


@register.filter
def space_after_capital(value):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", value)