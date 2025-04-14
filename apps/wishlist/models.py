from django.db import models
from django.contrib.auth.models import User
from apps.base.models import BaseModel


class Wishlist(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wishlist")
    books = models.ManyToManyField("book.Book", related_name="wishlists")

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
