from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
    return render(request, 'account/about.html')


def contact(request):
    return render(request, 'account/contact.html')


def doctors(request):
    return render(request, 'account/doctors.html')

def patients(request):
    return render(request, 'user/patients.html')

@login_required(login_url='login')
def news(request):
    return render(request, 'account/news.html')


def teamMembers(request):
    return render(request, 'user/teamMembers.html')

def appointment(request):
    return render(request, 'user/appointment.html')
