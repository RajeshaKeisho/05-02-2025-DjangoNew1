from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_employees),
    path('itdept/', views.it_department_employees),
    path('highsal/', views.high_salary_employees),
    path('rhdept/', views.hr_department_high_salary_employees),
    path('exclude/', views.exclude_high_salary_employees),
    path('avgsal/', views.avg_salary),
    # path('avgsalpd/', views.avg_salary_per_department),
    # path('numemp/', views.num_employees_per_department),
    path('most/', views.department_with_most_employees),
    # path('hrit/', views.hr_and_it_department_employees),
    path('salaryorname/', views.salary_or_name_contains),
    path('highpaid/', views.high_paid_employees),

]
