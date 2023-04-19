from rest_framework import serializers
from chats.models import ChatMessage


class ChatMessageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'text', 'msg_sender', 'msg_reciver', 'is_read']