from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postname = models.CharField(max_length=50)
    contents = models.TextField()
# Create your models here.
