from django.urls import path

from common_web_tools.web.views import index, sessions_view, raise_error, EmployesListView

urlpatterns = (

    path('', index, name='index'),
    path('sessions/', sessions_view, name='sessions view'),
    path('error/', raise_error, name='error'),
    path('employees/', EmployesListView.as_view(), name='employee list'),
)

from .signals import *