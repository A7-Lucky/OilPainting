from django.db import models
from users.models import User
from django_resized import ResizedImageField


# 변환시킬 모델
class Style(models.Model):
    category = models.CharField("카테고리 이름", max_length=100)
    
    def __str__(self):
        return self.category


class Image(models.Model):
    style = models.ForeignKey(Style, verbose_name="스타일", on_delete=models.SET_NULL, null=True)
    output_img = models.ImageField("결과사진", upload_to="media/articles/", null=True)
    
    def __str__(self):
        return f'{self.style}로 변환한 이미지 {self.output_img}'

class Article(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    image = models.CharField("결과사진", max_length=100)
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
