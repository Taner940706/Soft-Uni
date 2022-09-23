# 2. create url.py in the project
from django.urls import path

from department_app.departments.views import show_departments, redirect_to_first_department, show_not_found

urlpatterns = (
    path('', show_departments),
    #path('<department_id>/', show_departments_details),
    #path('int/<int:department_id>', show_departments_details)
    path('redirect/', redirect_to_first_department, name="show departments"),
    path('not-found/', show_not_found, name="not found")

)
