from django.shortcuts import render, redirect
from chats.models import ChatMessage
from chats.forms import MessageSubmitionForm
from django.contrib.auth.models import User
from chats.serializers import ChatMessageSerialzer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin_url')
def home(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'chats/home.html', context)

    
@api_view(['GET'])
def get_chats(request, receiver_id):
    if request.method == 'GET':
        chats = ChatMessage.objects.filter(
            Q(msg_sender=request.user.id) & Q(msg_receiver=receiver_id) |
            Q(msg_sender=receiver_id) & Q(msg_receiver=request.user.id)).order_by('-sended_on')
        serialize_chats = ChatMessageSerialzer(chats, many=True)
        return Response(serialize_chats.data, status=status.HTTP_200_OK)
    return Response({'error': 'something went wrong, failed to fetch data!'}, status=status.HTTP_408_REQUEST_TIMEOUT)


def save_chat(request):
    if request.method == 'POST':
        message_submition_form = MessageSubmitionForm(request.POST)
        if message_submition_form.is_valid():
            message_submition_form.save()
            return redirect('home_url')
    return Response(status=status.HTTP_400_BAD_REQUEST)


def delete_chat(request, chat_id):
    try:
        chat = ChatMessage.objects.get(pk=chat_id)
        chat.delete()
    except:
        pass
    
    return redirect('home_url')