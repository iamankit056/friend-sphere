from django.urls import path
from chats import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('user/<int:reciver_id>/chats/get', views.get_chats, name='get_chats_url'),
    path('user/<int:reciver_id>/chat/send', views.save_chat, name='save_chat_url'),
    path('user/chat/<int:chat_id>/delete', views.delete_chat, name='delete_chat_url'),
]
