from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', help_text="The groups this user belongs to", 
                                    blank=True, verbose_name='groups')
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text="Specific Permission for this user",
        verbose_name="user permissions"
    )
    