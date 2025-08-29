from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=100)

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