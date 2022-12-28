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
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!')
        else:
            messages.error(request, f'couldnt create account')
    return render(request, 'user/register.html')


def loginV(request):
    if request.method=="POST":
        user=authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            messages.success(request, f'Login success')
            
            if request.POST.get('next'):
                return redirect(request.POST.get('next').strip())
            else:
                return redirect('home')
        else:
            messages.error(request, f'Invalid username or passsword.')
    return render(request, 'user/login.html')


def Logout(request):
    logout(request)
    return render(request, 'user/home.html')




