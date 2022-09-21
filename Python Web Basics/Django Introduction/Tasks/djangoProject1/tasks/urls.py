from django.urls import path

from djangoProject1.tasks.views import get_all_tasks, testme, index

urlpatterns = (
    path('', index),
    path('it-works/', testme),
    path('all/', get_all_tasks),
)