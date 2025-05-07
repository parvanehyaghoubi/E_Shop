from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('register/', register, name='register'),
    path('signout/', signout, name='signout'),
]
