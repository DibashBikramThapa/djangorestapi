from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """user permissions to update"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """own status update"""

    def has_object_permission(self, request, view, obj):
        """check user to update own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
