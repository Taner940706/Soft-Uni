from django.http import HttpResponse
from django.shortcuts import render

from djangoProject3.web.forms import TodoCreatorForm, TodoForm, PersonCreatorForm
from djangoProject3.web.models import Person


def index(request):
    form_class = TodoForm
    if request.method == "GET":
        form = form_class()
    else:
        form = form_class(request.POST)
        if form.is_valid():
            return HttpResponse('All is valid')
    contex = {
        'form': form,
    }
    return render(request, 'index.html', contex)


def list_person(request):
    context = {
        'persons': Person.objects.all()
    }

    return render(request, 'list-persons.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreatorForm()
    else:
        form = PersonCreatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)
