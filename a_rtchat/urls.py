from django.urls import path
from.views import *
# Define your URL patterns here.

urlpatterns = [
    path('', chat_home, name='home'),
]