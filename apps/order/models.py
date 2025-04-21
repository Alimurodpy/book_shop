from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from apps.book.models import Book
from apps.base.models import BaseModel
import decimal


class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        PENDING = "PENDING", "Kutilmoqda"
        PROCESSING = "PROCESSING", "Jarayonda"
        SHIPPED = "SHIPPED", "Yuborilgan"
        DELIVERED = "DELIVERED", "Xaridorga berilgan"
        CANCELLED = "CANCELLED", "Bekor qilindi"

    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name="orders", verbose_name="Foydalanuvchi")
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING, verbose_name="Holati")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
    @property
    def total_amount(self):
        """Buyurtma elementlari asosida umumiy summani hisoblaydi"""
        total = sum( item.total_price for item in self.items.all() )
        return total if total is not None else decimal.Decimal("0.00")

    def __str__(self):
        user_info = f"({self.user})" if self.user else "(Foydalanuvchi o'chirilgan)"
        return f"Buyurtma #{self.id} {user_info} - {self.get_status_display()}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Buyurtma", related_name="items")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="order_items")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narx (buyurtma vaqtidagi)")
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name="Miqdori")

    class Meta:
        verbose_name = "Buyurtma elementi"
        verbose_name_plural = "Buyurtma elementlari"

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.book.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x '{self.book.title}' (Buyurtma #{self.order.id})"

    @property
    def total_price(self):
        return self.price * decimal.Decimal(self.quantity)
