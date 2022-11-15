import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


def very_slow_operation():
    return random.randint(1, 1048)


@cache_page(1*60)
def index(request):
    value = very_slow_operation()
    return HttpResponse(f'Value is: {value}')
