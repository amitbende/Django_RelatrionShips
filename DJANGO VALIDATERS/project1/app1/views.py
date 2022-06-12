from django.shortcuts import render, redirect
from .forms import EmployeesForm
from .models import Employees

# Create your views here.
def Employees_View(request):
    form = EmployeesForm()
    template_name = 'app1/employeesform.html'

    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showemployees_url')
    context = {'form': form}
    return render(request, template_name, context)

def Show_Employees(request):
    data = Employees.objects.all()
    template_name = 'app1/showemployees.html'
    context = {'obj': data}
    return render(request, template_name, context)