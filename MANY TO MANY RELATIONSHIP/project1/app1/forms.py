from django import forms
from .models import Owner, Car

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
