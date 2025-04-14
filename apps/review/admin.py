from django.contrib import admin
from .models import Review, Rating
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'text', 'created_at', 'updated_at')
    search_fields = ('book__title', 'user__username', 'text')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'book', 'user', 'stars', 'created_at', 'updated_at')
    search_fields = ('book__title', 'user__username')
    list_filter = ('stars', 'created_at')
    ordering = ('-created_at',)