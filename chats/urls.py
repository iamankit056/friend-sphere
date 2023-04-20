from django.urls import path
from chats import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('receiver/<int:receiver_id>/chats', views.get_chats, name='get_chats_url'),
    path('receiver/<int:receiver_id>/chat/send', views.save_chat, name='send_chat_url'),
    path('user/chat/delete', views.delete_chat, name='delete_chat_url'),
]
