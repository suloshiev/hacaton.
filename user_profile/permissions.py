from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Ограничения для не автаризованных пользователей'''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        '''Разрешение на запись только владельцу'''
        return obj.owner== request.user

