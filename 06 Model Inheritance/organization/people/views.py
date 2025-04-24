from django.shortcuts import render
from django.views.generic import ListView
from .models import EmployeeProxy, CustomerProxy

# View to list all employees
class EmployeeListView(ListView):
    model = EmployeeProxy
    template_name = 'people/employee_list.html'
    context_object_name = 'employees'  

# View to list all customers
class CustomerListView(ListView):
    model = CustomerProxy
    template_name = 'people/customer_list.html'
    context_object_name = 'customers'  
