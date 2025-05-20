from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsGroupMember(permissions.BasePermission):
    def __init__(self, group_name):
        self.group_name = group_name
    
    def has_permission(self, request, view):
        return request.user.groups.filter(name=self.group_name).exists()