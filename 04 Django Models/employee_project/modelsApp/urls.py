from django.urls import path
from modelsApp import views

urlpatterns = [
    path("data/", views.employeeView, name="employee"),
]
