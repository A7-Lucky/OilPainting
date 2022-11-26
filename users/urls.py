from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("profile/", views.ProfileView.as_view(), name="profile_view"),
    path("api/token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/change-password/", views.ChangePasswordView.as_view(), name="change-password"),  # 비밀번호 변경
    path("api/password_reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),  # 비밀번호 리셋
    # kakao
    path("kakao/login/", views.kakao_login, name="kakao_login"),
    path("kakao/callback/", views.kakao_callback, name="kakao_callback"),
    path("kakao/login/finish/", views.KakaoLogin.as_view(), name="kakao_login_todjango"),
]
