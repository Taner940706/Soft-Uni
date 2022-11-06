from django.urls import path

from cbv.web.views import ViewAsTemplate

urlpatterns = (
    path('', ViewAsTemplate.as_view()),
)