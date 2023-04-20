from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
def home(request):
    users = User.objects.all()
    profiles = User.objects.all()

    context = {
        'users': users,
        'profiles': profiles
    }

    return render(request, 'chats/home.html', context)


