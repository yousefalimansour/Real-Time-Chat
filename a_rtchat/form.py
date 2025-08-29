from django import forms
from django.forms import ModelForm
from .models import ChatMessage

class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add message ...', 'class': 'p-4 text-black', 'maxlength': '300', 'autofocus': True}),
        }