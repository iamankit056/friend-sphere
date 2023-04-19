from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Profile
from users.serializers import UserSerializer, ProfileSerializer

# Create your views here.
def signup(request):
    return render(request, 'users/signup.html')


def signin(request):
    return render(request, 'users/login.html')


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialize_user = UserSerializer(users, many=True)    
    profiles = Profile.objects.all()
    serialize_profile = ProfileSerializer(profiles, many=True)

    json_data = {
        'users': serialize_user.data,
        'profiles': serialize_profile.data
    }

    return Response(json_data, status=status.HTTP_200_OK)

