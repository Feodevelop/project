from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    userimage = models.URLField(max_length=200)
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
# Create your models here.