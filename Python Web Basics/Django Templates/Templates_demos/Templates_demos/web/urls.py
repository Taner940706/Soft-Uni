from django.urls import path

from Templates_demos.web.views import index, redirect_to_home

urlpatterns = [
    path('', index, name='index'),
    path('go-to-home', redirect_to_home, name='redirect to home')
]