# 2. create url.py in the project
from django.urls import path

from department_app.departments.views import show_departments

urlpatterns = (
    path('', show_departments),
    #path('<department_id>/', show_departments_details),
    #path('int/<int:department_id>', show_departments_details)

)
