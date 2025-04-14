from rest_framework import serializers

from apps.book.models import Book
from .models import Review, Rating
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'book', 'user', 'text')
        extra_kwargs = {
            'book': {'read_only': True},
            'user': {'read_only': True}
        }


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('book', 'user', 'stars')
        read_only_fields = ('book', 'user')


class TopRatedSerializer(serializers.ModelSerializer):
    avg_ratings = serializers.FloatField(source='avg_rating')
    baho_soni = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'avg_ratings', 'baho_soni')