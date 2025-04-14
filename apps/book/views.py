from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer, BookUploadImageSerializer
from .paginations import MyPageNumberPagination
from .filters import CustomBookFilter
# from .permissions import IsOwner



class BookListAPIView(ListAPIView):
    permission_classes = []
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = MyPageNumberPagination


class BookCreateAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookRetrieveAPIView(RetrieveAPIView):
    permission_classes = []
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def delete(self, request):
        instance = self.get_object()
        book_id = instance.id
        self.perform_destroy(instance)
        return Response(
            {"message": f"ID si - {book_id} bo'lgan ma'lumot o'chirildi"},
            status=status.HTTP_200_OK
        )
    
class BookSearchAPIView(ListAPIView):
    permission_classes = []
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CustomBookFilter
    search_fields = ['@title', '^author']
    ordering_fields = ['created_at', 'price']
        

class BookUploadImageAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookUploadImageSerializer

    def perform_create(self, serializer):
        book_id = self.kwargs['pk']
        book = get_object_or_404(Book, id=book_id)
        serializer.save(book=book)
