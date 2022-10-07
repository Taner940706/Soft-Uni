from django.shortcuts import render, get_object_or_404, redirect

from djangoProject2.Web.models import Employee


def index(request):
   # x = list(Employee.objects.all())
   # print(x)
   # pass
   employees2 = Employee.objects.filter(first_name='Maria').order_by('years_of_experience')
   context = {
       'employees': Employee.objects.all(),
       'employees2': employees2
   }

   return render(request, 'index.html', context)
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')