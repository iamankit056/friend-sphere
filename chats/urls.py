from django.urls import path
from chats import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('messages/<int:user_id>', views.chat_messages, name='chat_messages_url'),
]
