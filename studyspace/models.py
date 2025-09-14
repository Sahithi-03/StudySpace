from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    txt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

