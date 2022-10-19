from django.urls import path

from djangoProject3.web.views import index, list_person, create_person

urlpatterns = (
    path('', index, name='index'),
    path('persons/', list_person, name='list person'),
    path('persons/create/', create_person, name='create person')
)