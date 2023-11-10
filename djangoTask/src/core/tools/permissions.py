from djangoTask.src.core.enums.enums import UserProfile
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsRoleAdminOrReadOnly(BasePermission):
    def __init__(self, role):
        self.role = role

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # For GET, HEAD or OPTIONS
            return True
        else:  # For POST, PUT or DELETE
            user = request.user
            return user.is_authenticated and (self.role in user.user_type or user.is_superuser)


class IsRoleAdmin(BasePermission):
    def __init__(self, role):
        self.role = role

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (self.role in user.user_type or user.is_superuser)


class IsSupplierAdminOrReadOnly(IsRoleAdminOrReadOnly):
    def __init__(self):
        super().__init__(UserProfile.SUPPLIER)


class IsSupplierAdmin(IsRoleAdmin):
    def __init__(self):
        super().__init__(UserProfile.SUPPLIER)


class IsCarDealerAdminOrReadOnly(IsRoleAdminOrReadOnly):
    def __init__(self):
        super().__init__(UserProfile.CAR_DEALER)


class IsCarDealerAdmin(IsRoleAdmin):
    def __init__(self):
        super().__init__(UserProfile.CAR_DEALER)


class IsClientAdminOrReadOnly(IsRoleAdminOrReadOnly):
    def __init__(self):
        super().__init__(UserProfile.CLIENT)

