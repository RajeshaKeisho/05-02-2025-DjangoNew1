from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<html><body><h1>ABUT US</h1><p>This is the bout Page</body></html>")


def sample_view(request):
    if "error" in request.GET:
        raise ValueError("This is a sample ValueError")
    return HttpResponse("NO Error Occurred")