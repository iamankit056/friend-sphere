from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import status
from users.forms import ProfileUpdationForm, UserUpdationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    return render(request, 'users/signup.html')


def signin(request):
    return render(request, 'users/signin.html')


@login_required(login_url='signin_url')
def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except: 
        messages.info(request, f'{username} does not exist')
        return render(request, 'errors/404.html', status=status.HTTP_404_NOT_FOUND)

    readonly = '' if username == request.user.username else 'readonly'
    context = {
        'user_profile': user,
        'readonly': readonly
    }
    return render(request, 'users/profile.html', context)   


@login_required()
def update_profile(request):
    if request.method == 'POST':
        user_updation_form = UserUpdationForm(request.POST, instance=request.user)
        request.user.profile.profile_pic.delete(False)
        profile_updation_form = ProfileUpdationForm(request.POST, request.FILES, instance=request.user.profile)

        if user_updation_form.is_valid() and profile_updation_form.is_valid():
            user_updation_form.save()
            profile_updation_form.save()
            messages.success(request, f'{request.user.username} profile updated sucessesfully...')

        else:
            messages.error(request, f'{request.user.username} profile updation failed...')

    return redirect('user_profile_url', username=request.user.username)