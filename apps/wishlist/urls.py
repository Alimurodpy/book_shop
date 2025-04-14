from django.urls import path
from .views import WishlistView, AddBookToWishlistView, RemoveBookFromWishlistView

# 1. `POST /api/Wishlist/`  - Wishlistga kitob qo‘shish
# 2. `GET /api/Wishlist/`   -  Wishlistni ko‘rish
# 3. `DELETE /api/Wishlist/{id}/`  -  Wishlistdan kitobni olib tashlash
urlpatterns = [
    path("", WishlistView.as_view(), name="Wishlist"),
    path("add/", AddBookToWishlistView.as_view(), name="Wishlist_add"),
    path("delete/<int:pk>/", RemoveBookFromWishlistView.as_view(), name="Wishlist_remove"),
]
