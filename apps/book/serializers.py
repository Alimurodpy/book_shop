from  rest_framework import serializers
from .models import Book, BookImage

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['image']

class BookSerializer(serializers.ModelSerializer):
    book_images = BookImageSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'price', 'description', 'book_images']

class BookUploadImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = ['id', 'image', 'created_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'id': {'read_only': True}
        }