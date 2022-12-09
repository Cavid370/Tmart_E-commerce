from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to = 'user_avatars', blank = True, null = True )

class BlockedIP(models.Model):
    ip_addr = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.ip_addr

class SubscriberEmail(models.Model):
    email = models.EmailField(unique = True)
    def __str__(self):
        return self.email        