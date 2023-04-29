from django import forms
from chats.models import ChatMessage


class MessageSubmitionForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['text', 'msg_sender', 'msg_receiver']