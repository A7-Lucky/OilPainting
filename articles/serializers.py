from rest_framework import serializers
from articles.models import Article, Comment, Style, Image

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__" 


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    def get_username(self,obj):
        return obj.user.username
    
    class Meta:
        model = Comment
        fields = "__all__"
        
class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source="comment_set")
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = "__all__"