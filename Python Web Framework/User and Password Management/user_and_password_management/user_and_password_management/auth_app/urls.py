from django.contrib.auth.views import LoginView
from django.urls import path

from user_and_password_management.auth_app.views import SignUpView, SignInView, SignOutView

urlpatterns = (

    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
)