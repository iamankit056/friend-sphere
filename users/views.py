from django.shortcuts import render
from users.models import Profile
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    return render(request, 'users/signup.html')


def signin(request):
    return render(request, 'users/login.html')


