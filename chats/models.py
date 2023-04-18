from django.db import models
from users.models import Profile

class ChatMessage(models.Model):
    text = models.TextField(blank=True)
    file = models.FileField(upload_to='messages', blank=True)
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_sender')
    msg_reciver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_reciver')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'chat {self.pk}'