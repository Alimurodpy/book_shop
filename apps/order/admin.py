from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ["book", "price", "quantity"]
    readonly_fields = ["price"]


    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user", "status","total_amount", "created_at"]
    list_filter = ["status"]
    search_fields = ["user__first_name", "user__last_name", "user__email"]
    ordering = ["-created_at"]
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "order", "book", "price", "quantity", "total_price"]
    search_fields = ["book__title"]
    ordering = ["-order__created_at"]
