from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Qo'shimcha maydonlar, masalan foydalanuvchi username va email
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email', read_only=True)

    def validate(self, attrs):
        # Tokenni olishdan oldin validation qilish
        data = super().validate(attrs)

        # Foydalanuvchi haqida qo'shimcha ma'lumotlarni token bilan birga qaytarish
        data['username'] = self.user.username
        data['email'] = self.user.email

        return data
    

# Foydalanuvchi registratsiya serializeri
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']