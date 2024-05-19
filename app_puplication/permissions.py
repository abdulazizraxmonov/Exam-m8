from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it,
    while allowing anyone to read (GET) the object.
    """
    def has_permission(self, request, view):
        # Allow anyone to view (GET) the list or detail view.
        if view.action in ['list', 'retrieve']:
            return True
        # Otherwise, require authentication
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow anyone to view (GET) individual items
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object
        return obj.user == request.user
