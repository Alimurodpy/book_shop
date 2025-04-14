from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
        Foydalanuvchi faqat o'z obyektlariga kirish huquqiga ega
    """
    def has_object_permission(self, request, view, obj):
        # Foydalanuvchi obyekt egasi bo'lishi kerak
        return obj.owner == request.user