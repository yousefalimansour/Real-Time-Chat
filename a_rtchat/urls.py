from django.urls import path
from.views import *
# Define your URL patterns here.

urlpatterns = [
    path('', chat_home, name='home'),
    path('chat/<username>',get_or_create_chatroom, name='start-chat'),
    path('chat/room/<chatroom_name>', chat_home, name='chatroom'),
]

