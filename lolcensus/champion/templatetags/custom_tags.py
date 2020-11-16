from django import template

register = template.Library()


@register.filter
def slash_to_breakline(value):
    return value.replace("/", " /<br>")