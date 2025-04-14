from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomTokenObtainPairView, LogoutView, UserInfoView, RegisterView, UserUpdateView

# 1. `POST /api/auth/register/` – Ro‘yxatdan o‘tish
# 2. `POST /api/auth/login/` – Kirish
# 3. `POST /api/auth/logout/` – Chiqish
# 4. `GET /api/auth/profile/` – Profilni ko‘rish
# 5. `PUT /api/auth/profile/update/`

urlpatterns = [
    # Token olish uchun
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Tokenni yangilash uchun
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserInfoView.as_view(), name='user_info'),
    path('profile/update/', UserUpdateView.as_view(), name='user_info_update'),
    path('register/', RegisterView.as_view(), name='register'),

]

