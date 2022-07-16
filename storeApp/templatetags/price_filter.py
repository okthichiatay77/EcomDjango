from django import template


register = template.Library()

@register.filter(name='filter_price')
def filter_price(value):
    # x = ''
    # c = 0
    # for i in str(value)[::-1]:
    #     c += 1
    #     if c == 3:
    #         x = ',' + i + x
    #         c = 0
    #     else:
    #         x = i + x
    #
    # if x[0] == ',':
    #     return x[1:]
    return f'{value:,}'
