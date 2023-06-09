from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    bio = models.TextField(default='Hi there, I am using friend-share')

    def __str__(self):
        return self.user.username
    