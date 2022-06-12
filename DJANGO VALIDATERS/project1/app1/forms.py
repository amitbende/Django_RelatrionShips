from django import forms
from .models import Employees
from django.core import validators

class EmployeesForm(forms.ModelForm):
    salary = forms.FloatField(validators=[validators.MinValueValidator(1000), validators.MaxValueValidator(20000)])
    
    class Meta:
        model = Employees
        fields = '__all__'

    def clean_eid(self):
        value = self.cleaned_data['eid']
        if value < 0 or value > 30:
            raise validators.ValidationError('Eid Value Is Incorrect !!!')
        return value

    def clean_salary(self):  
        value = self.cleaned_data['salary']
        if value < 1000 or value > 20000:
            raise validators.ValidationError('Please Give Salary More Than 1000 And Less Than 20000.')
        return value

    def clean_name(self):
        value = self.cleaned_data['name']
        if value.istitle() != True:
            raise validators.ValidationError('First Character is Small !!!')
        return value

    def clean(self):
        all_data = super().clean()
        pass1 = all_data['password']
        pass2 = all_data['c_password']
        if pass1 != pass2:
            raise validators.ValidationError('Password and C_password Are Different !!!')