from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
]