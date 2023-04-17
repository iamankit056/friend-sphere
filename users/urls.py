from django.urls import path
from chats import views

urlpatterns = [
    path('login', views.home, name='login_url'),
    path('signup', views.home, name='signup_url'),
]
