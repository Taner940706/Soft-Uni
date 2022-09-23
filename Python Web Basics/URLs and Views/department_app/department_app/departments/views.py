from random import choice

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


#def show_departments(request, *args, **kwargs):
 #   body = f' path: {request.path}, args = {args} and kwargs = {kwargs}'
  #  return HttpResponse(body)


#def show_departments_details(request, department_id):
 #   order_by = request.GET('order_by', 'name')
  #  body = f' path: {request.path}, id: {department_id}, order_by = {order_by}'
   # return HttpResponse(body)


# with render
def show_departments(request, *args, **kwargs):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),
   }


    return render(request, 'departments/all.html', context)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)

    return redirect('show departments')


def show_not_found(request):
    raise Http404('Not found!')
#    return HttpResponseNotFound('This is not found')
