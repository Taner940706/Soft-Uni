from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic as views

def index(request):
    print(
        authenticate(username='taner', password='ismail')
    )
    new_user = User.objects.create_user(
        username='taner',
        password='ismail',

    )
    user_messages = '' if request.user.is_authenticated else 'not '
    return HttpResponse(f'The user is {user_messages} authenticated!')


def create_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='taner',
        password='ismail',
    )

    #create session
    login(request, user)

#Ways to create users in Django
#1 terminal: python manage.py createsuperuser
#2. If you have at least one user, create from Django Admin Panel
#3 With code: 'User.objects.create_user()' or 'User.objects.create_superuser()'


#function-based views
@login_required(login_url='/login')
def show_profile(request):
    return HttpResponse('you are {request.user}')

#class-based views
class ProfileView(LoginRequiredMixin, views.View):
    def get(self):
        return HttpResponse(f'your are {self.request.username}')