from django.db import models
from apps.book.models import Book
from apps.base.models import BaseModel
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator     

class Review(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    text = models.TextField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Sharh'
        verbose_name_plural = 'Sharhlar'

    def __str__(self):
        return f"{self.user.username}'s review for {self.book.title}"

class Rating(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ratings')
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Yulduzlar'
    )

    class Meta:
        indexes = [
            models.Index(fields=['stars']), 
        ]
        unique_together = ('book', 'user')
        ordering = ['-stars']
        verbose_name = 'Baholash'
        verbose_name_plural = 'Baholashlar'

    def __str__(self):
        return f"{self.user.username}'s rating for ({self.book.id}){self.book.title}"