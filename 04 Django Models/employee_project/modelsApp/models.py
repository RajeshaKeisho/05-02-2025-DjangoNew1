from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Employee object with E-No: {self.ename}"

