from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class CheckRole(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        if obj.close_account:
            return False
        return request.method in SAFE_METHODS



class IsArchiveOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        return obj.archive.owner == request.user


class StoryPermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        owner = obj.author
        if owner == request.user:
            return True
        if owner.close_account:
            return False
        return request.method in SAFE_METHODS
