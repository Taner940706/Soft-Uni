from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic as views


class UserListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = User
    template_name = 'web/index.html'
