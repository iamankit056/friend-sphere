from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import status
from users.forms import ProfileUpdationForm, UserUpdationForm
from django.contrib.auth import authenticate,login, logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["passw1"]
        confirmpassword = request.POST["passw2"]
        if(password1 != confirmpassword):
            messages.warning(request, "Passwords is incorrect")
            return redirect('/signup')
        try:
            if user.objects.get(username=username):
                messages.info(request, "username is taken")
                return redirect('/signup')
        except:
            pass

        try:
            if user.objects.get(email=email):
                messages.info(request, "email is taken")
                return redirect('/signup')

        except:
            pass 
        user = User.objects.create_user(
            username=username, password=password1, email=email )
        user.save()
    
        messages.success(request, f"Account created successfull for {username}")
        return redirect( "/signin")
    return render(request, 'users/signup.html')


def signin(request):
     if request.method == "POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(username=uname,password=password)
        if myuser is not None:
            login(request,myuser) 
            messages.success(request,"signin successful")
            return redirect("/")
        else:
            messages.error(request,"login failed")
            return redirect("/signin")

    return render(request, 'users/signin.html')

def logout(request):
    logout(request)
    messages.info(request,"signout successful")
    return redirect("/")


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