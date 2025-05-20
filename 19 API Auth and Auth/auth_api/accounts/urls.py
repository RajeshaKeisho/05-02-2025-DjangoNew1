from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    TokenRefreshView,
    GroupViewSet,
    PermissionViewSet,
    UserViewSet,
    AssignGroupToUserView,
    RemoveGroupFromUserView
)

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('assign-group/<int:user_id>/<int:group_id>/', AssignGroupToUserView.as_view(), name='assign_group'),
    path('remove-group/<int:user_id>/<int:group_id>/', RemoveGroupFromUserView.as_view(), name='remove_group'),
    path('', include(router.urls)),
]