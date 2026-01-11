from rest_framework.permissions import BasePermission

class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'candidate'
        )


class IsRecruiterForJob(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.job.posted_by == request.user
            or request.user.is_staff
        )
