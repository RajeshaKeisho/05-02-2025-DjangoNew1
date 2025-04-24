from django.db import models
from decimal import Decimal
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True  

    def __str__(self):
        return self.name

class Employee(Person):
    employee_id = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()

class Customer(Person):
    customer_id = models.CharField(max_length=10, unique=True)
    join_date = models.DateField()


class EmployeeProxy(Employee):
    class Meta:
        proxy = True
        ordering = ['name']
    def is_senior(self):
        """Check if employee has been working for more than 5 years."""
        from datetime import date
        return (date.today() - self.hire_date).days > 5 * 365


class CustomerProxy(Customer):
    class Meta:
        proxy = True
        ordering = ['-join_date']   
    def is_loyal(self):
        """Check if customer has been a member for more than 3 years."""
        from datetime import date
        return (date.today() - self.join_date).days > 3 * 365

