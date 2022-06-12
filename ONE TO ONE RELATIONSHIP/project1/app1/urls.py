from django.urls import path
from. import views

urlpatterns = [
    path('pv/', views.PersonView),
    path('av/', views.AdharView)
]