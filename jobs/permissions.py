from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'recruiter'


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.posted_by == request.user
            or request.user.is_staff
        )
