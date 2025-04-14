from django.urls import path
from .views import ReviewListCreateView, ReviewDeleteView, RatingView, TopRatedView

# 3. GET /api/books/{id}/reviews/ – Kitob sharhlarini olish
# 1. POST /api/books/{id}/reviews/ – Kitobga sharh qo'shish
# 4. DELETE /api/reviews/{id}/ – Sharhni o'chirish (faqat muallifi yoki admin)
# 2. POST /api/books/{id}/rate/ – Kitobni baholash (1-5 yulduz)
# 5. GET /api/books/top-rated/ – Eng yuqori baholangan kitoblar ro'yxati

urlpatterns = [
    path('<int:pk>/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('<int:pk>/rate/', RatingView.as_view(), name='rating'),
    path('top-rated/', TopRatedView.as_view(), name='top-rated'),

]