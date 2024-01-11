from rest_framework.permissions import SAFE_METHODS, BasePermission

from djangoTask.src.core.enums.enums import UserProfile


class IsSupplierAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            user = request.user
            return user.is_authenticated and (
                (UserProfile.SUPPLIER in user.user_type) or user.is_superuser
            )


class IsSupplierAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (
            (UserProfile.SUPPLIER in user.user_type) or user.is_superuser
        )


class IsCarDealerAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            user = request.user
            return user.is_authenticated and (
                (UserProfile.CAR_DEALER in user.user_type) or user.is_superuser
            )


class IsCarDealerAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (
            (UserProfile.CAR_DEALER in user.user_type) or user.is_superuser
        )


class IsClientAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            user = request.user
            return user.is_authenticated and (
                (UserProfile.CLIENT in user.user_type) or user.is_superuser
            )
