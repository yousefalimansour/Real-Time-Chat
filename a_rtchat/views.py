from django.shortcuts import render,get_object_or_404,redirect
from .models import ChatGroup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .form import ChatMessageForm
from django.http import Http404
# Create your views here.

@login_required
def chat_home(request, chatroom_name='3nab'):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:40]
    form = ChatMessageForm()

    other_user = None
    if chat_group.is_private:     
        if request.user not in chat_group.members.all():
            raise Http404("You are not allowed to access this chatroom.")
        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break


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
        
    context = {
        'chat_messages': chat_messages, 
        'form': form,
        'chatroom_name': chatroom_name,
        'other_user': other_user,
    }

    return render(request, 'a_rtchat/chat.html', context)


@login_required
def get_or_create_chatroom(request, username):
    if username == request.user.username:
        return redirect('home')
    
    other_user = User.objects.get(username=username)
    chatrooms = ChatGroup.objects.filter(is_private=True)

    if chatrooms.exists():
        for chatroom in chatrooms:
            members = chatroom.members.all()
            if other_user in members and request.user in members:
                return redirect('chatroom', chatroom_name=chatroom.group_name)
    chatroom = ChatGroup.objects.create(is_private=True)
    chatroom.members.add(request.user, other_user)

    return redirect('chatroom', chatroom.group_name)
