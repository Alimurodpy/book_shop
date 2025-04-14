from rest_framework import serializers
from apps.book.models import Book
from .models import Wishlist
from apps.book.serializers import BookSerializer


class WishlistSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ("id", "user", "books")


class WishlistToAddBookSerializer(serializers.Serializer):
    # Faqat bodydagi book_id ni kutadi va validatsiya qiladi
    book_id = serializers.IntegerField()

    def validate_book_id(self, value):
        """Kitob mavjudligini tekshirish"""
        if not Book.objects.filter(id=value).exists():
            raise serializers.ValidationError("Bunday IDga ega kitob mavjud emas.")
        return value
