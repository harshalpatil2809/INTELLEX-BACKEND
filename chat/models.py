from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    ROLE_CHOICES = (
        ('user','User'),
        ('ai','AI')
    )
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE,related_name='message')
    role = models.CharField(max_length=10,choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)