# has_permission() - view-level permissions
# has_object_permission() - Instamce-level permissions
from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
