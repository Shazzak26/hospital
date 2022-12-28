from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.loginV, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.register, name='register'),

]