from  rest_framework import serializers
from .models import Book, BookImage
from apps.review.serializers import ReviewSerializer, RatingSerializer
from django.db.models import Avg

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['image']

class BookSerializer(serializers.ModelSerializer):
    book_images = BookImageSerializer(many=True, read_only=True)
    book_reviews = ReviewSerializer(many=True, read_only=True)
    avg_ratings = serializers.SerializerMethodField()

    def get_avg_ratings(self, obj):
        ratings = obj.book_ratings.all()
        if ratings.exists():
            return ratings.aggregate(Avg('stars'))['stars__avg']
        return None

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'price', 'description', 'book_images', 'book_reviews', 'avg_ratings']

class BookUploadImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = ['id', 'image', 'created_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'id': {'read_only': True}
        }