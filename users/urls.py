from django.urls import path
from users import views

urlpatterns = [
    path('signin', views.signin, name='signin_url'),
    path('signup', views.signup, name='signup_url'),
    path('get_users/', views.get_users, name='get_users_url'),
]
