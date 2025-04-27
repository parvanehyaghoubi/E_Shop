from django.urls import path
from .views import index, shop, detail, cart, checkout, contact, login, register

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('detail/', detail, name='detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
