from rest_framework import serializers

from apps.book.models import Book
from .models import Order, OrderItem
from apps.book.serializers import BookSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['book', 'quantity', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_amount',  'items', 'created_at' ]
        read_only_fields = ['id', 'created_at', 'user', 'status', 'total_amount']

class OrderCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), write_only=True)
    quantity = serializers.IntegerField(write_only=True, default=1)
    old_quantity = serializers.IntegerField(source='book.quantity', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'book', 'quantity', 'old_quantity', 'book_title']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Order
        fields = ['user', 'status', 'items']
        read_only_fields = ['user', 'items']

    def get_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(items, many=True).data