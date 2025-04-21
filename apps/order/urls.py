from django.urls import path
from .views import (
    OrderListView,
    OrderCreateAPIView, 
    OrderDetailView, 
    OrderCancelView, 
    OrderStatusUpdateView,
    OrderHistoryView
)

urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path("create/", OrderCreateAPIView.as_view(), name="order-create"),
    path("<int:pk>/order/", OrderDetailView.as_view(), name="order-detail"),
    path("<int:pk>/cancel/", OrderCancelView.as_view(), name="order-cancel"),
    path("<int:pk>/status/", OrderStatusUpdateView.as_view(), name="order-status-update"),
    path("history/", OrderHistoryView.as_view(), name="order-history"),    
]