from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Doctors/', views.doctors, name='doctors'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('patients/', views.patients, name='patients'),
    path('appointment/', views.appointment, name='appointment'),
    path('teamMembers/', views.teamMembers, name='teamMembers'),
]