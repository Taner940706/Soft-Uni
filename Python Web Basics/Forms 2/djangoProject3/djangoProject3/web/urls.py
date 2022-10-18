from django.urls import path

from djangoProject3.web.views import index

urlpatterns = (
    path('', index, name='index'),
)