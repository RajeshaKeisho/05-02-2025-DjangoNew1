from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet
from user_profiles import views as profile_views
from user_profiles.views import CustomLoginView

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/profile/', profile_views.profile, name='profile'),  # Ensure this path is correct
    path('register/', profile_views.register, name='register'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
