from django.urls import path
from chats import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('get_chats/<int:user_id>', views.get_chats, name='get_chats_url'),
]
