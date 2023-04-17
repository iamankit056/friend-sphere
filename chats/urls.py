from django.urls import path
from chats import views

urlpatterns = [
    path('', views.home, name='home_url'),
]
