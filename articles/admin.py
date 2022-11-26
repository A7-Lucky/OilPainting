from django.contrib import admin
from articles.models import Article, Comment, Style, Image

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Style)
admin.site.register(Image)

