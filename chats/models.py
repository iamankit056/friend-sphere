from django.db import models
from users.models import Profile
from django.utils import timezone

class ChatMessage(models.Model):
    text = models.TextField(blank=True)
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_sender')
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_receiver')
    sended_on = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.msg_sender} => {self.msg_receiver}'
