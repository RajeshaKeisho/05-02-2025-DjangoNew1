from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_premium = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    is_premium_content = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title