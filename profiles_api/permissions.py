from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # Method가 안전한 메소드면 True를 반환한다 <- Get method
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id