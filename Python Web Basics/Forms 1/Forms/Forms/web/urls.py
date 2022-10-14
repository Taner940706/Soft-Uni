from django.urls import path

from Forms.web.views import index

urlpatterns=(
    path('', index, name='index'),
)