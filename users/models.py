from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    userimage = models.URLField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenum = models.CharField(max_length=12)
    name = models.CharField(max_length=12)
# Create your models here.