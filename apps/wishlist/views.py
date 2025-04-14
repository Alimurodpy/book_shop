from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.book.models import Book
from .models import Wishlist
from .serializers import WishlistSerializer, WishlistToAddBookSerializer


class WishlistView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)


class AddBookToWishlistView(APIView):

    def post(self, request):
        user = request.user
        serializer = WishlistToAddBookSerializer(data=request.data)

        if serializer.is_valid():
            book_id = serializer.validated_data["book_id"]
            book = get_object_or_404(Book, id=book_id)
            wishlist, created = Wishlist.objects.get_or_create(user=user)

            if book not in wishlist.books.all():
                wishlist.books.add(book)
                response_serializer = WishlistSerializer(wishlist)
                return Response(
                    data=response_serializer.data, status=status.HTTP_200_OK
                )
            return Response(
                    {"message": "Kitob allaqachon istaklar ro'yxatida mavjud."},
                    status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveBookFromWishlistView(DestroyAPIView):
    def delete(self, request, pk):
        user = request.user
        book = get_object_or_404(Book, id=pk)
        wishlist = get_object_or_404(Wishlist, user=user)

        if book in wishlist.books.all():
            wishlist.books.remove(book)
            return Response({"message": "Kitob istaklar ro'yxatidan o'chirildi."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Kitob istaklar ro'yxatida topilmadi."}, status=status.HTTP_404_NOT_FOUND)

