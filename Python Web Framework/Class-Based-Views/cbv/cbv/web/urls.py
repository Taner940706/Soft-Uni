from django.urls import path

from cbv.web.views import ViewAsTemplate, EmployeeCreateView, EmployeeUpdateView

urlpatterns = (
    path('', ViewAsTemplate.as_view()),
    path('create/', EmployeeCreateView.as_view(), name='employee create'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee update'),
)