from django.contrib import admin
from .models import Book, Category, BookImage

class ImageAdmin(admin.TabularInline):
    model = BookImage
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category')
    search_fields = ('id', 'title', 'author')
    inlines = [ImageAdmin]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
