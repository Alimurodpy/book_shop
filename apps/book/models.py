from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth.models import User

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(BaseModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'

    def __str__(self):
        return self.title

class BookImage(BaseModel):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_images')
    image = models.ImageField(upload_to='book_images/')

    class Meta:
        verbose_name = 'Kitob rasmi'
        verbose_name_plural = 'Kitob rasmlari'
    def __str__(self):
        return self.book.title