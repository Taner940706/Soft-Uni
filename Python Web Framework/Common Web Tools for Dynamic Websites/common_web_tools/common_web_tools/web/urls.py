from django.urls import path

from common_web_tools.web.views import index

urlpatterns = (

    path('', index, name='index'),
)
