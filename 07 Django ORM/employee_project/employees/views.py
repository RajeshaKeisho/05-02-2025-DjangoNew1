from django.shortcuts import render
from django.db.models import Avg, Count
from django.db.models import Q
from .models import Employee, Department
from django.db import connection
def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all.html', {'employees': employees})

def it_department_employees(request):
    it_employees = Employee.objects.filter(department__name='IT')
    return render(request, 'employees/it_department_employees.html', {'it_employees': it_employees})

def high_salary_employees(request):
    high_salary_employees = Employee.objects.filter(salary__gt=55000)
    return render(request, 'employees/high_salary_employees.html', {'high_salary_employees': high_salary_employees})

def hr_department_high_salary_employees(request):
    hr_high_salary_employees = Employee.objects.filter(department__name='HR', salary__gte=55000)
    return render(request, 'employees/hr_department_high_salary_employees.html', {'hr_high_salary_employees': hr_high_salary_employees})

def exclude_high_salary_employees(request):
    excluded_employees = Employee.objects.exclude(salary__gt=60000)
    return render(request, 'employees/exclude_high_salary_employees.html', {'excluded_employees': excluded_employees})

def avg_salary(request):
    avg_salary = Employee.objects.aggregate(avg_salary=Avg('salary'))
    return render(request, 'employees/avg_salary.html', {'avg_salary': avg_salary})


def department_with_most_employees(request):
    department = Department.objects.annotate(num_employees=Count('employee')).order_by('-num_employees').first()
    return render(request, 'employees/department_with_most_employees.html', {'department': department})

def salary_or_name_contains(request):
    employees = Employee.objects.filter(Q(name__icontains='John') | Q(salary__gte=60000))
    return render(request, 'employees/employee_list.html', {'employees': employees})

def high_paid_employees(request):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM employees_employee WHERE salary > 60000")
        employees = cursor.fetchall()

 
    employee_objects = [Employee(*row) for row in employees]

    return render(request, 'employees/employee_list.html', {'employees': employee_objects})

