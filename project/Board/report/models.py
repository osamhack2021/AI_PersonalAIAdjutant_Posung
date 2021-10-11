from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Report(models.Model):
    author = models.CharField(max_length=10, null=False)
    rank = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    content2 = models.TextField(null=False)
    content3 = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
