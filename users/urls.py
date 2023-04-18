from django.urls import path
from users import views

urlpatterns = [
    path('login', views.login, name='login_url'),
    path('signup', views.signup, name='signup_url'),
]
