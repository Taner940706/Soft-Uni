from django.urls import path

from djangoProject2.Web.views import index, delete_employee

urlpatterns = (
    path('', index, name='index'),
    path('delete<int:pk>/', delete_employee, name='delete employee'),
)
