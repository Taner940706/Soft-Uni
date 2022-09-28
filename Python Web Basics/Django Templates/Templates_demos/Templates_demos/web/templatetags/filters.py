from datetime import datetime

from django.template import Library

register = Library()


@register.filter('odd')
def get_odd(values):
    return [x for x in values if x % 2 == 1]


@register.filter('add_date_style')
def date_styler(date):
    return date.strftime("%Y/%m/%d")