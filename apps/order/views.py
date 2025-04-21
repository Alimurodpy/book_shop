from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.base.permissions import IsOwner
from apps.book.models import Book
from apps.order.models import Order, OrderItem
from .serializers import OrderCreateSerializer, OrderSerializer, OrderItemSerializer, OrderStatusUpdateSerializer


class OrderListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user).exclude(status__in=['CANCELLED', 'DELIVERED'])

class OrderCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        book = serializer.validated_data['book']
        quantity = serializer.validated_data.get('quantity', 1)

        if book.quantity < quantity:
            raise ValidationError({"error": "Kitoblar soni yetarli emas"})
        
        book.quantity -= quantity
        book.save()

        order, _ = Order.objects.get_or_create(user=user, status='PENDING')

        serializer.save(order=order)

class OrderDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return super().get_queryset().exclude(status='CANCELLED')
    
class OrderCancelView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.status = Order.OrderStatus.CANCELLED
        order.save()
        return Response({"message": "Kitob bekor qilindi."}, status=status.HTTP_204_NO_CONTENT)

class OrderStatusUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderStatusUpdateSerializer
    queryset = Order.objects.all()


class OrderHistoryView(ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user, status='DELIVERED')