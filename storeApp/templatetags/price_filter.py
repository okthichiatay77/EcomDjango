from django import template


register = template.Library()

@register.filter(name='filter_price')
def filter_price(value):
    return f'{value:,}'
