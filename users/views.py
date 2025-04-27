from django.shortcuts import render


def login(request):
    return render(request, template_name='login.html')


def register(request):
    return render(request, template_name='register.html')
