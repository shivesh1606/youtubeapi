from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid

class Vedio(models.Model):
    id = models.AutoField(primary_key=True)
    key=models.CharField(max_length=20050, null=True)
    date=models.DateField(auto_now=False, auto_now_add=False)
    link = models.CharField(max_length=20050, null=True)
    title = models.CharField(max_length=10000, blank=True, null=True)
    description=models.CharField(max_length=10000, blank=True, null=True)
    def __str__(self):
        return str(self.title)