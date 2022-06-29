from django import template

register = template.Library()

@register.filter(name='filter_range')
def filter_range(value):
    return value[:100] + '...'