from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def admin_login(request):
    return render(request, 'HR/admin_login.html')


def index(request):
    return render(request, "HR/index.html")


def add_patient(request):
    return render(request, "HR/add_patients.html")

def add_doctor(request):
    return render(request, "HR/plusDoctors.html")

def workers(request):
    return render(request, "HR/workers.html")


def add_appointment(request):
    return render(request, "HR/add_appointment.html")