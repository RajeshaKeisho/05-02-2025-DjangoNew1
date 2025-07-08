from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for user profile (e.g., profile picture, bio, etc.)

    def __str__(self):
        return self.user.username + ' Profile'

