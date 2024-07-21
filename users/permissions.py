from rest_framework.permissions import BasePermission


class UserPermissionsDestroy(BasePermission):
    """Удаление пользователя доступно суперюзеру."""
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False


class IsManager(BasePermission):
    """Доступно менеджерам."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager').exists()

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='manager').exists():
            return True
        return False


class UserIsOwner(BasePermission):
    """Доступно владельцам."""

    def has_object_permission(self, request, view, obj):
        return request.user == obj
