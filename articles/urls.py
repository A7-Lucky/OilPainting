from django.urls import path
from articles import views


urlpatterns = [
    path("", views.ArticleView.as_view()),
    path("<article_id>/", views.ArticleDetailView.as_view()), 
    path("comment/", views.CommentView.as_view()),
    path("comment/<comment_id>/", views.CommentView.as_view()),
] 