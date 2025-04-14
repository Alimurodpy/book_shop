from django.urls import path
from .views import (BookListAPIView, 
                    BookCreateAPIView, 
                    BookRetrieveAPIView, 
                    BookUpdateDestroyAPIView,
                    BookSearchAPIView,
                    BookUploadImageAPIView
)

urlpatterns = [
    path('', BookListAPIView.as_view(), name='books'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
    path('<int:pk>/upload-image/', BookUploadImageAPIView.as_view(), name='book_image'),
    path('<int:pk>/', BookRetrieveAPIView.as_view(), name='book_detail'),
    path('<int:pk>/update-delete/', BookUpdateDestroyAPIView.as_view(), name='book_update'),
    path('search/', BookSearchAPIView.as_view(), name='book_search'),

]