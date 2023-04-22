from django.shortcuts import render
from chats.models import ChatMessage
from users.models import Profile
from chats.serializers import ChatMessageSerialzer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    users_profile = Profile.objects.all()
    context = {
        'users_profile': users_profile
    }
    return render(request, 'chats/home.html', context)


@api_view(['GET'])
def get_chats(request, receiver_id):
    if request.method == 'GET':
        sender_chats = ChatMessage.objects.filter(msg_sender=request.user.id, msg_receiver=receiver_id)
        reciver_chats = ChatMessage.objects.filter(msg_sender=receiver_id, msg_receiver=request.user.id)
        serialize_sender_chats = ChatMessageSerialzer(sender_chats, many=True)
        serialize_reciver_chats = ChatMessageSerialzer(reciver_chats, many=True)
        json_data = {
            'sender_messages': serialize_sender_chats.data,
            'serialize_reciver_chats': serialize_reciver_chats.data
        }
        return Response(json_data, status=status.HTTP_200_OK)
    return Response({'error': 'something went wrong, failed to fetch data!'}, status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(['POST'])
def save_chat(request, receiver_id):
    if request.method == 'POST':
        request.data['msg_sender'] = request.user.id
        request.data['msg_receiver'] = receiver_id
        serialize_chat = ChatMessageSerialzer(data=request.data)
        if serialize_chat.is_valid():
            serialize_chat.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_chat(request, chat_id):
    try:
        chat = ChatMessage.objects.get(pk=chat_id)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)