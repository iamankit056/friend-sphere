from django.urls import path
from users import views

urlpatterns = [
    path('signin', views.signin, name='signin_url'),
    path('signup', views.signup, name='signup_url'),
    path('user/<str:username>', views.show_profile, name='show_profile_url'),
    path('user/<str:username>/edit', views.edit_profile, name='edit_profile_url'),
]
