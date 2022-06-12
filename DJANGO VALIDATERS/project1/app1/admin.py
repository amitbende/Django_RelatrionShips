from django.contrib import admin
from .models import Employees

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['eid', 'name', 'mail', 'salary', 'password', 'c_password']
admin.site.register(Employees, EmployeesAdmin)
