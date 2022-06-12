from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Owner, Car
from .forms import OwnerForm, CarForm

# Create your views here.
def Owner_View(request):
    form = OwnerForm()
    template_name = 'app1/ownerform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('<h1 style="color:green;"> Data Saved !!! <h1>')
            return redirect('ownerdata_url')
    return render(request, template_name, context)

def Car_View(request):
    form = CarForm()
    template_name = 'app1/carform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('<h1 style="color:green;"> Data Saved !!! <h1>')
            return redirect('cardata_url')
    return render(request, template_name, context)

def Show_Owner(request):
    data = Owner.objects.all()
    template_name = 'app1/showowner.html'
    context = {'obj': data}
    return render(request, template_name, context)

def Show_Car(request):
    data = Car.objects.all()
    template_name = 'app1/showcar.html'
    context = {'obj': data}
    return render(request, template_name, context)
