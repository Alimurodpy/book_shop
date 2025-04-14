from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Count

from apps.book.models import Book
from apps.base.permissions import IsOwner
from django.contrib.auth.models import User
from .serializers import ReviewSerializer, RatingSerializer, TopRatedSerializer
from .models import Review, Rating



class ReviewListCreateView(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        book = self.kwargs["pk"]
        return Review.objects.filter(book=book)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs["pk"])
        serializer.save(user=self.request.user, book=book)


class ReviewDeleteView(DestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    queryset = Review.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"success": "Review muvaffaqiyatli o'chirildi!"},
            status=status.HTTP_204_NO_CONTENT,
        )


class RatingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        user = request.user
        stars = request.data.get("stars")

        if stars is None or stars not in ['1', '2', '3', '4', '5']:
            return Response(
                {"error": "Yulduzlar 1 dan 5 gacha bo'lishi kerak!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        raiting, created = Rating.objects.get_or_create(
            book=book, user=user, defaults={"stars": stars}
        )

        serializer = RatingSerializer(raiting)

        if created:
            return Response(
                {"message": "Baho berildi", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            raiting.stars = stars
            raiting.save()
            return Response(
                {"message": "Baho yangilandi", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
class TopRatedView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TopRatedSerializer

    def get_queryset(self):
        return Book.objects.annotate(
            avg_rating=Avg('book_ratings__stars'),
            baho_soni=Count('book_ratings')
        ).filter(baho_soni__gt=0).order_by('-avg_rating')
