from django.shortcuts import render
from django import http

from djangoProject1.tasks.models import Task


# Create your views here.


def testme(request):
    return http.HttpResponse("it works")


def get_all_tasks(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f"{t.name}({t.id})" for t in all_tasks)
    return http.HttpResponse(result)


def index(request):
    all_tasks = Task.objects.all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)