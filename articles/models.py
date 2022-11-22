from django.db import models
from users.models import User


class Article(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    image = models.CharField("결과사진", max_length=100)
    title = models.CharField(verbose_name="제목", max_length=30)
    content = models.CharField(verbose_name="내용", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f'{self.user} / {self.title}')

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    article =  models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="댓글", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.user} / {self.comment}")