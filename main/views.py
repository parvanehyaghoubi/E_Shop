from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def cart(request):
    return render(request, template_name='cart.html')


def checkout(request):
    return render(request, template_name='checkout.html')


def contact(request):
    return render(request, template_name='contact.html')


