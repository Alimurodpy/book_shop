import django_filters
from .models import Book

class CustomBookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'min_price', 'max_price']