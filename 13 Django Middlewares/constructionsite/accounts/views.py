from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<html><body><h1>ABOUT US </h1><p>This is the about Page!</p></body></html>")

def sample_view(request):
    if 'error' in request.GET:
        raise ValueError("This is a sample Value Error")
    return HttpResponse("No Error Occurred")