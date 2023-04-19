from django.shortcuts import render, redirect
from users.models import Profile
from chats.models import ChatMessage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chats.serializers import ChatMessageSerialzer

# Create your views here.
def home(request):
    return render(request, 'chats/home.html')


@api_view(['GET', 'POST', 'DELETE'])
def chat_messages(request, user_id):

    # /messages/user_id => GET
    if request.method == 'GET':
        chat_messages = ChatMessage.objects.filter(msg_sender=request.user.pk, msg_reciver=user_id)
        serialize_chat_messages = ChatMessageSerialzer(chat_messages, many=True)

        return Response(serialize_chat_messages.data, status=status.HTTP_200_OK)
    
    # /messages/user_id => POST
    if request.method == 'POST':
        serialize_chat_messages = ChatMessageSerialzer(data=request.data)
        if serialize_chat_messages.is_valid():
            serialize_chat_messages.save()
            return Response(serialize_chat_messages.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)  

    # /messages/user_id => DELETE
    if request.method == 'DELETE':
        try:
            chat_messages = ChatMessage.objects.get(pk = request.data['pk'])
            chat_messages.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
