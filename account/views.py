from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
    return render(request, 'account/about.html')


def contact(request):
    return render(request, 'account/contact.html')


def doctors(request):
    return render(request, 'account/doctors.html')

@login_required(login_url='login')
def news(request):
    return render(request, 'account/news.html')


