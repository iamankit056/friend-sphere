from django.urls import path
from users import views

urlpatterns = [
    path('signin', views.signin, name='signin_url'),
    path('signup', views.signup, name='signup_url'),
    path('signout', views.signout, name='signout_url'),
    path('user/<str:username>', views.user_profile, name='user_profile_url'),
    path('user/profile/updation', views.update_profile, name='update_profile_url'),
    path('user/<str:username>/delete', views.delete_user, name='delete_user_url'),
]
