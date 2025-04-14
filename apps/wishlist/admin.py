from django.contrib import admin
from .models import Wishlist

# Register your models here.


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "get_book_count", "get_book_title")

    def get_book_count(self, obj):
        return obj.books.count()

    get_book_count.short_description = "Number of Books"

    def get_book_title(self, obj):
        return ", ".join([book.title for book in obj.books.all()])

    get_book_title.short_description = "Book Title"
