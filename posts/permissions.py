from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Permisions for author in blog posts"""

    def has_permission(self, request, view):
        """if user is authenticated (loggged)"""
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """If user is admin can do whatever"""
        if request.user.is_staff:
            return True
        """If the user isn't the author only SAFE METHODS are available"""
        """ SAFE_METHODS: GET, HEAD or OPTIONS requests """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
