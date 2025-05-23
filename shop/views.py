from django.shortcuts import render
from .models import Shop
from django.core.paginator import Paginator


def shop_list(request):
    lists = Shop.objects.all().filter(is_published=True)
    paginator = Paginator(lists, per_page=3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'shop_lists': paged_listings
    }
    return render(request, template_name='shop.html', context=context)
