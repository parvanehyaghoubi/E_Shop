from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login(request):
    return render(request, template_name='login.html')


def register(request):
    return render(request, template_name='register.html')


def signout(request):
    logout(request)
    return redirect('login')
