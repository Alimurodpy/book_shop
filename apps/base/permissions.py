from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Foydalanuvchi faqat o'z obyektlariga kirish huquqiga ega
    """

    def has_permission(self, request, view):
        # Umuman kirish huquqini beradi, faqat autentifikatsiyadan o'tgan bo'lsa
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Faqat o'zining obyektlari uchun ruxsat
        return obj.user == request.user
