from django.shortcuts import render
from users.models import Profile
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    return render(request, 'users/signup.html')


def signin(request):
    return render(request, 'users/login.html')


def show_profile(request, username):
    profile = Profile.objects.get(user=User.objects.get(username=username))
    context = {
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)


def edit_profile(request, username):
    return render(request, 'user/edit-profile.html')
