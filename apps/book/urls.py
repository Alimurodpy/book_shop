from django.urls import path
from .views import (BookListAPIView, 
                    BookCreateAPIView, 
                    BookRetrieveAPIView, 
                    BookUpdateDestroyAPIView,
                    BookSearchAPIView,
                    BookUploadImageAPIView
)

# 1. `GET /api/books/` – Barcha kitoblarni olish
# 2. `POST /api/books/` – Yangi kitob qo‘shish (admin)
# 3. `POST /api/books/{id}/upload-image/` – Kitob uchun rasm yuklash
# 4. `GET /api/books/{id}/` – Bitta kitobni olish
# 5. `PUT /api/books/{id}/` – Kitobni yangilash (admin)
# 6. `DELETE /api/books/{id}/` – Kitobni o‘chirish (admin)
# 7. `GET /api/books/search/?q=...` – Kitoblarni nomi yoki muallifiga qarab qidirish

urlpatterns = [
    path('', BookListAPIView.as_view(), name='books'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
    path('<int:pk>/upload-image/', BookUploadImageAPIView.as_view(), name='book_image'),
    path('<int:pk>/', BookRetrieveAPIView.as_view(), name='book_detail'),
    path('<int:pk>/update-delete/', BookUpdateDestroyAPIView.as_view(), name='book_update'),
    path('search/', BookSearchAPIView.as_view(), name='book_search'),

]