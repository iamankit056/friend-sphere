from django.shortcuts import render
from users.models import Profile
from chats.models import ChatMessage
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'chats/home.html')


def get_chats(request, user_id):
    users_profile = Profile.objects.all().values()
    chats_messages = ChatMessage.objects.filter(msg_sender=request.user.pk, msg_reciver=user_id).values()

    data = {
        'users_profile': users_profile,
        'chats_messages': chats_messages
    }


    return JsonResponse(data=data)