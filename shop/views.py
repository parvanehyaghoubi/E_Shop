from django.shortcuts import render
from .models import Shop


def shop_list(request):
    lists = Shop.objects.all().filter(is_published=True)
    context = {
        'shop_lists': lists
    }
    return render(request, template_name='shop.html', context=context)
