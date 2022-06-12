from django.urls import path
from . import views

urlpatterns = [
    path('ef/', views.Employees_View, name='employeesform_url'),
    path('se/', views.Show_Employees, name='showemployees_url')
]