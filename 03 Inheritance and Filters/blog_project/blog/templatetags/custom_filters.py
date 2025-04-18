from django import template
import re

register = template.Library()

@register.filter
def uppercase(value):
    """Converts a string to uppercase."""
    return value.upper()

@register.filter
def word_count(value):
    """Counts the number of words in a string."""
    return len(value.split())

@register.filter
def first_word(value):
    """Returns the first word of a string."""
    return value.split()[0] if value else ''

@register.filter
def last_word(value):
    """Returns the last word of a string."""
    return value.split()[-1] if value else ''

@register.filter
def remove_punctuation(value):
    """Removes punctuation from the string."""
    return re.sub(r'[^\w\s]', '', value)

@register.filter
def reverse_string(value):
    """Reverses the string."""
    return value[::-1]

@register.filter
def word_limit(value, num):
    """Limits the content to a given number of words."""
    words = value.split()
    return ' '.join(words[:num]) + ('...' if len(words) > num else '')

@register.filter
def char_count(value):
    """Counts the number of characters (excluding whitespace)."""
    return len(value.replace(" ", ""))
