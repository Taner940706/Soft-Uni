from django.urls import path

from user_and_password_management.web.views import UserListView

urlpatterns = (

    path('', UserListView.as_view(), name='index'),
)