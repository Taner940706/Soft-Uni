from django.urls import path

from unit_and_integration_testing.web.views import ProfilesListView

urlpatterns = (

    path('', ProfilesListView.as_view(), name='list profiles'),
)