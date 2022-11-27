from rest_framework import serializers
from articles.models import Article, Comment, Style, Image


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Image
        fields = "__all__"


# 아티클 조회
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    bookmarks = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    def get_likes(self, obj):
        return obj.likes.count()

    def get_bookmarks(self, obj):
        return obj.bookmarks.count()

    class Meta:
        model = Article
        fields = "__all__"


# 아티클 생성
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "title",
            "content",
            "image",
        )


# 댓글 조회
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Comment
        fields = "__all__"


# 댓글 생성
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("comment",)
