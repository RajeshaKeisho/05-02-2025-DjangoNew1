from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_employees),
    path('itdept/', views.it_department_employees),
    path('highsal/', views.high_salary_employees),
    path('avgsalpd/', views.avg_salary_per_department),
    path('most/', views.department_with_most_employees),
    path('highpaid/', views.high_paid_employees),
]