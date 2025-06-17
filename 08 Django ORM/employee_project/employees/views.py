from django.shortcuts import render
from django.db.models import Avg, Count
from django.db.models import Q
from .models import Employee, Department
from django.db import connection


# Create your views here.

def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all.html', {'employees':employees})
    
def it_department_employees(request):
    it_employees = Employee.objects.filter(department__name='IT')
    return render(request, 'employees/it_department_employees.html', {'it_employees': it_employees})

def high_salary_employees(request):
    high_salary_employees = Employee.objects.filter(salary__gt=55000)
    return render(request, 'employees/high_salary_employees.html', {'high_salary_employees': high_salary_employees})


def avg_salary_per_department(request):
    # Calculate the average salary per department
    departments = Department.objects.annotate(avg_salary=Avg('employee__salary'))
    return render(request, 'employees/avg_salary_per_department.html', {'departments': departments})

def department_with_most_employees(request):
    department = Department.objects.annotate(num_employees=Count('employee')).order_by('-num_employees').first()
    return render(request, 'employees/department_with_most_employees.html', {'department': department})


def high_paid_employees(request):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM employees_employee WHERE salary > 60000")
        employees = cursor.fetchall()

 
    employee_objects = [Employee(*row) for row in employees]

    return render(request, 'employees/employee_list.html', {'employees': employee_objects})
