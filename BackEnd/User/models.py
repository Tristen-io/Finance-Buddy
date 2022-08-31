from django.db import models

from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    


