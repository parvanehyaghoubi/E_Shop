from django.shortcuts import render
from .models import Listing


def listings(request):
    products = Listing.objects.all().filter(is_published=True)[0]
    context = {
        'listings': products
    }
    return render(request, template_name='detail.html', context=context)

#
# def detail(request):
#     return render(request, template_name='detail.html')
