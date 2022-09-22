from django.http import HttpResponse
from django.shortcuts import render


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
