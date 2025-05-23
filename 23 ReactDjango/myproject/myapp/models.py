# myapp/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_available = models.BooleanField(default=False)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.name

