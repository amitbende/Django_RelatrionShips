from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm, CourseForm
from .models import Student, Course

# Create your views here.
def Student_view(request):
    form = StudentForm()
    template_name = 'app1/studentform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1 style="color:green;"> Data Saved !!! </h1>')
    return render(request, template_name, context)

def Course_view(request):
    form = CourseForm()
    template_name = 'app1/courseform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1 style="color:green;"> Data Saved !!! </h1>')
    return render(request, template_name, context)

def Show_Student(request):
    data = Student.objects.all()
    template_name = 'app1/showstudent.html'
    context = {'obj': data}
    return render(request, template_name, context)

def Show_Course(request):
    data = Course.objects.all()
    template_name = 'app1/showcourse.html'
    context = {'obj': data}
    return render(request, template_name, context)
