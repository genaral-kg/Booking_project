from rest_framework.permissions import BasePermission

# TODO: PERMISSION - TO USER
class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner