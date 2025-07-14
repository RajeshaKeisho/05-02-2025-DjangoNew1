# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def times(value, arg):
    """Multiplies a value by the argument."""
    return value * arg

