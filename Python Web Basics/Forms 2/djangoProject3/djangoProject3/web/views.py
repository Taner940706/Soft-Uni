from django.http import HttpResponse
from django.shortcuts import render

from djangoProject3.web.forms import TodoCreatorForm


def index(request):
    if request.method == "GET":
        form = TodoCreatorForm()
    else:
        form = TodoCreatorForm(request.POST)
        if form.is_valid():
            return HttpResponse('All is valid')
    contex = {
        'form': form,
    }
    return render(request, 'index.html', contex)
