from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
