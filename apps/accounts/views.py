from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, UserUpdateSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class LogoutView(APIView):
    """
    LogoutView - bu view foydalanuvchini chiqarish uchun ishlatiladi.
    ---
    responses:
      200:
        description: Foydalanuvchi chiqarildi
    """
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user=request.user)
        for token in tokens:
            BlacklistedToken.objects.get_or_create(token=token)
        return Response({"message": "Logged out successfully"})
    


class UserInfoView(APIView):
    """
    UserInfoView - bu view foydalanuvchini haqida ma'lumot olish uchun ishlatiladi.
    ---
    responses:
      200:
        description: Foydalanuvchi haqida ma'lumot
    """
    def get(self, request, *args, **kwargs):
        # Foydalanuvchi haqida ma'lumot olish
        user = request.user  # Avtomatik tarzda foydalanuvchi olinadi
        user_data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
        return Response(user_data)

class RegisterView(APIView):
    """
    RegisterView - bu view foydalanuvchini ro'yxatdan o'tish uchun ishlatiladi.
    ---
    responses:
      201:
        description: Foydalanuvchi ro'yxatdan muvaffaqiyatli qo'shildi
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserUpdateView(APIView): 
    """
    UserUpdateView - bu view foydalanuvchini ma'lumotlarni o'zgartirish uchun ishlatiladi.
    ---
    responses:
      200:
        description: Foydalanuvchi ma'lumotlari o'zgartirildi
    """   
    def patch(self, request):
        serializer = UserUpdateSerializer(instance = request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    