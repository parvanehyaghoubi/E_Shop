from django.urls import path
from .views import *

urlpatterns = [
    path('detail/', listings, name='detail'),
]
