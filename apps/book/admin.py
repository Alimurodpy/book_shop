from django.contrib import admin
from .models import Book, Category, BookImage
from apps.review.models import Review, Rating

class ImageAdmin(admin.TabularInline):
    model = BookImage
    extra = 1

class ReviewAdmin(admin.TabularInline):
    model = Review
    extra = 1

class RatingAdmin(admin.TabularInline):
    model = Rating
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'quantity', 'category')
    search_fields = ('id', 'title', 'author')
    list_filter = ('category', 'created_at')
    list_per_page = 10
    ordering = ('created_at',)
    inlines = [ImageAdmin, ReviewAdmin, RatingAdmin]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
