from django.db import models
from django.conf import settings

# Create your models here.

class Blogviewsets(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

