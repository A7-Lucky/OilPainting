from django.urls import path, include
from articles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.ArticleViewSet)

urlpatterns = [
    path("viewset/", include(router.urls)),
    path("", views.ArticleView.as_view(), name="article_view"),
    path("<int:article_id>/", views.ArticleDetailView.as_view(), name="article_detail_view"),
    path("<int:article_id>/comment/", views.CommentView.as_view(), name="comment_view"),
    path("<int:article_id>/comment/<int:comment_id>/", views.CommentDetailView.as_view(), name="comment_detail_view"),
    path("like/<int:article_id>/", views.LikeView.as_view(), name="like_view"),
    path("bookmark/<int:article_id>/", views.BookmarkView.as_view(), name="bookmark_view"),
    path("mybookmark/", views.MybookmarkView.as_view(), name="my_bookmark_view"),
    path("myarticle/", views.MyarticleView.as_view(), name="my_article_view"),
    path("<int:article_id>/user/", views.ArticleUserView.as_view(), name="article_user_view"),
]
