from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    friends = models.ManyToManyField('Friend', related_name='my_friends', blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile}'
