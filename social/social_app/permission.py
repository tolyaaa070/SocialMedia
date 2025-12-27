from rest_framework import permissions

class CheckRole(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.close_account:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

