from django.urls import path, include
from articles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ArticleViewSet)

urlpatterns = [
    path('viewset/',include(router.urls)),
    path("", views.ArticleView.as_view()),
    path("<article_id>/", views.ArticleDetailView.as_view()), 
    path("comment/", views.CommentView.as_view()),
    path("comment/<comment_id>/", views.CommentView.as_view()),
] 