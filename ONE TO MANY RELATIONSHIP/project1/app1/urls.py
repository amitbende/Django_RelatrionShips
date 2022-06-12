from django.urls import path
from . import views

urlpatterns = [
    path('sv/', views.Student_view),
    path('cv/', views.Course_view),
    path('ss/', views.Show_Student),
    path('sc/', views.Show_Course)
]