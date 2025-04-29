from django.shortcuts import render


def detail(request):
    return render(request, template_name='detail.html')
