from django.shortcuts import render
from .forms import PersonForm, AdharForm

# Create your views here.
def PersonView(request):
    form = PersonForm()
    template_name = 'app1/personform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name, context)

def AdharView(request):
    form = AdharForm()
    template_name = 'app1/adharform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = AdharForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name, context)

