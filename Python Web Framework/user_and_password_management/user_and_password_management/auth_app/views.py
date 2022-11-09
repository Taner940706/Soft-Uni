from django.contrib.auth import forms as auth_forms, views as auth_views, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "username",)
        field_classes = {"username": auth_forms.UsernameField}


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('sign up')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'
