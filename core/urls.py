from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('apps.book.urls')),
    path('api/auth/', include('apps.accounts.urls')),
    path('api/wishlist/', include('apps.wishlist.urls')),
    path('api/reviews/', include('apps.review.urls')),
    path('api/orders/', include('apps.order.urls')),
    # path('api/admin/', include('apps.admin.urls')),
]

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BOOK SHOP REST API",
        default_version='v1',
        description="API hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]