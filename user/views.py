from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import signupform

def home(request):
    return render(request, 'user/home.html')



def register(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save



    return render(request, 'user/register.html')


def loginV(request):
    
    return render(request, 'user/login.html')


def Logout(request):
    logout(request)
    return render(request, 'user/home.html')



