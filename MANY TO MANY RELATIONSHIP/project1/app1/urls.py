from django .urls import path
from . import views

urlpatterns = [
    path('of/', views.Owner_View, name='ownerform_url'),
    path('cf/', views.Car_View, name='carform_url'),
    path('so/', views.Show_Owner, name='ownerdata_url'),
    path('sc/', views.Show_Car, name='cardata_url')
]