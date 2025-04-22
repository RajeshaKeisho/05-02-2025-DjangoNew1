from django.urls import path
from .views import employeeView

urlpatterns = [
    path("employees/", employeeView, name='employees'),
]