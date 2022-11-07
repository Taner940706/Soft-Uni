from django.urls import path

from Authentication.web.views import index, create_and_login, show_profile, ProfileView

urlpatterns = (
    path('', index, name='index'),
    path('create_user/', create_and_login, name='create and login user'),
    path('profile/1/', show_profile, name='show profile 1'),
    path('profile/2', ProfileView.as_view(), name='show profile 2'),
)

