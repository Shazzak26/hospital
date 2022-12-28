from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),
    path('index/', views.index, name='index'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('workers/', views.workers, name='workers'),
]