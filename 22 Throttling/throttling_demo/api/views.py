from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import PremiumUserThrottle

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        elif self.action == 'list':
            if self.request.user.is_authenticated and self.request.user.is_premium:
                throttle_classes = [PremiumUserThrottle]
            else:
                throttle_classes = [AnonRateThrottle, UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

class CustomLoginView(LoginView):
    template_name = 'api/login.html'
    
    def get_success_url(self):
        return '/api/'

# @login_required
def home_view(request):
    return render(request, 'api/home.html')

# @login_required
def books_view(request):
    return render(request, 'api/books.html')

# @login_required
def throttle_test_view(request):
    return render(request, 'api/throttle_test.html')