from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registration(request):
    return HttpResponse("<p>Registration Page</p>")

def login(request):
    return HttpResponse("<p>Login Page</p>")

def logout(request):
    return HttpResponse("<p>Logout Page</p>")
