from django.db import models
from django.contrib.auth.models import User
import shortuuid

# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True, default=shortuuid.uuid)
    user_online = models.ManyToManyField(User, related_name='online_in_group', blank=True)
    members = models.ManyToManyField(User, related_name='chat_group', blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name
    
class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.author}: {self.body}"