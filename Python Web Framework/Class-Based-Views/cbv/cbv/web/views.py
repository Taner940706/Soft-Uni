import random

from django import views
from django.http import HttpResponse
from django.shortcuts import render

from cbv.web.models import Employee


# class IndexView:
#
#     def __init__(self):
#         self.value = [random.randint(1, 15),]
#
#     @classmethod
#     def get_view(cls):
#         instance = IndexView()
#         the_view = instance.view
#         print(the_view)
#         return the_view
#
#     def view(self, request):
#         return HttpResponse(f'it works!: {self.value}')
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.value.append(random.randint(15, 30))


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': "CBV",
        }
        return render(request, 'base.html', context)


class ViewAsTemplate(views.generic.TemplateView):
    template_name = 'base.html'
    extra_context = {
        'title': 'Template View',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = Employee.objects.all()
        return context


class ViewTemplateWithListView(views.generic.ListView):
    context_object_name = 'employees'
    model = Employee
    template_name = 'base.html'
    extra_context = {
        'title': 'List View',
    }