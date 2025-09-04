from django.urls import path ,re_path
from .consumers import ChatRoomConsumer

websocket_urlpatterns = [
    # path("ws/chatroom/<chatroom_name>/", ChatRoomConsumer.as_asgi()),
    re_path(r'^ws/chatroom/(?P<chatroom_name>[^/]+)/?$', ChatRoomConsumer.as_asgi()),

]
