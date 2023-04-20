from django.urls import path
from chats import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('user/chats', views.get_chats, name='get_chats_url'),
    path('user/chat/send', views.save_chat, name='save_chat_url'),
    path('user/chat/delete', views.delete_chat, name='delete_chat_url'),
]
