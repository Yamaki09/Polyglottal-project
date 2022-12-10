from django.db import models

class Post(models.Model):
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    details = models.TextField()

