from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',),  # 초기 화면 구현 관련 정보 부족
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('dj_rest_auth.urls')),
    path('users/', include('allauth.urls')),
    path('articles/', include('articles.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)