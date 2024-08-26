from django.db import models
from posts.models import Post
from django.contrib.auth.models import User 

class Reviews(models.Model):
    postreview = models.ForeignKey(Post, on_delete=models.CASCADE)
    reviewname = models.CharField(max_length=50)
    reviewcontents = models.TextField()
    reviewuser = models.OneToOneField(User, on_delete=models.CASCADE)
# Create your models here.
