import random

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

CLICK_COUNT_SESSION_KEY = 'CLICK_COUNT_SESSION_KEY'


def very_slow_operation():
    return random.randint(1, 1048)


@cache_page(1*60)
def index(request):
    clicks_count = request.session.get(CLICK_COUNT_SESSION_KEY, 0) + 1
    request.session[CLICK_COUNT_SESSION_KEY] = clicks_count
    value = very_slow_operation()
    return HttpResponse(f'Value is: {value}')


def sessions_view(request):
    clicks_count = request.session.get(CLICK_COUNT_SESSION_KEY, 0) + 1
    request.session[CLICK_COUNT_SESSION_KEY] = clicks_count
    return HttpResponse(f'Clicks: {clicks_count}')


def raise_error(request):
    get_user_model().objects.get(pk=1012555)
