from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CustomLoginView, home_view, books_view, throttle_test_view
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LogoutView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # Template views
    path('home/', home_view, name='api-home'),
    # path('home/', home_view, name='api-home-alt'),  # Add this alternative path
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='api-home'), name='logout'),
    path('books/', books_view, name='api-books'),
    path('throttle-test/', throttle_test_view, name='api-throttle-test'),
]