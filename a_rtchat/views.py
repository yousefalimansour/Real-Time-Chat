from django.shortcuts import render,get_object_or_404,redirect
from .models import ChatGroup
from django.contrib.auth.decorators import login_required
from .form import ChatMessageForm
# Create your views here.

@login_required
def chat_home(request):
    chat_group = get_object_or_404(ChatGroup, group_name='3nab')
    chat_messages = chat_group.chat_messages.all()[:40]
    form = ChatMessageForm()

    if request.htmx:
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_messages = form.save(commit=False)
            chat_messages.group = chat_group
            chat_messages.author = request.user
            chat_messages.save()
            context = {
                'message': chat_messages,
                'user': request.user
            }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context)
    return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages, 'form': form})