from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
]
