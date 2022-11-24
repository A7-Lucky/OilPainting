# Generated by Django 4.1.3 on 2022-11-24 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="JPEG",
                        keep_meta=True,
                        quality=-1,
                        scale=None,
                        size=[300, 300],
                        upload_to="article",
                    ),
                ),
                ("title", models.CharField(max_length=30, verbose_name="제목")),
                ("content", models.CharField(max_length=100, verbose_name="내용")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bookmarks",
                    models.ManyToManyField(
                        related_name="article_bookmarks", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        related_name="article_likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.CharField(max_length=100, verbose_name="댓글")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_article",
                        to="articles.article",
                        verbose_name="게시글",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
            ],
        ),
    ]
