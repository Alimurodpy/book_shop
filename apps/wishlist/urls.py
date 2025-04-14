from django.urls import path
from .views import WishlistView, AddBookToWishlistView, RemoveBookFromWishlistView

urlpatterns = [
    path("", WishlistView.as_view(), name="Wishlist"),
    path("add/", AddBookToWishlistView.as_view(), name="Wishlist_add"),
    path("delete/<int:pk>/", RemoveBookFromWishlistView.as_view(), name="Wishlist_remove"),
]
