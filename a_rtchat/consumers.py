from channels.generic.websocket import WebsocketConsumer
from .models import ChatGroup,ChatMessage
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
import json

class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.chatroom_name = self.scope["url_route"]["kwargs"]["chatroom_name"]
        self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)

        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name,
            self.channel_name
        )

    def receive(self, text_data):
        # Handle incoming WebSocket messages
        text_data_json = json.loads(text_data)
        body = text_data_json['body']

        message = ChatMessage.objects.create(
            group=self.chatroom,
            author=self.user,
            body=body
        )
        event = {
                'type': 'message_handler',
                'message_id': message.id,
            }

        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name,
            event
        )

    def message_handler(self, event):
        message = get_object_or_404(ChatMessage, id=event['message_id'])
        context = {
            'message': message,
            'user': self.user,
        }
        html = render_to_string('a_rtchat/partials/chat_message_p.html', context=context)
        self.send(text_data=html)

