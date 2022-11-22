from django.urls import path
from articles import views


urlpatterns = [
    path("", views.ArticleView.as_view(), name="article_view"),
    # path("<article_id>/", views.ArticleView.as_view()),
    path("like/<int:article_id>/", views.LikeView.as_view(), name="like_view"),
    path("bookmark/<int:article_id>/", views.BookmarkView.as_view(), name="bookmark_view"),
]