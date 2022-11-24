from django.db import models
from users.models import User
from django_resized import ResizedImageField


class Article(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    image = ResizedImageField(size=[256, 256], upload_to="article", force_format="JPEG")
    title = models.CharField(verbose_name="제목", max_length=30)
    content = models.CharField(verbose_name="내용", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="article_likes")
    bookmarks = models.ManyToManyField(User, related_name="article_bookmarks")

    def __str__(self):
        return str(f"{self.user} / {self.title}")


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE, related_name="comment_user")
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE, related_name="comment_article")
    comment = models.CharField(verbose_name="댓글", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.user} / {self.comment}")
