from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from articles.models import Article, Comment, Style, Image
from articles.serializers import ArticleSerializer, CommentSerializer
from articles.utils import inference

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all().order_by("created_at")
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def post(self, request):
        data = request.data 
        output_img = inference(
                input=request.FILES["input"].read(),
                style=request.data.get("style", "") 
            )
        data = {
            "user" : request.user.username,
            "image" : output_img,
            "title" : request.data["title"],
            "content" : request.data["content"]
        }
        
        image_info = Image.objects.create(output_img=output_img)
        image_info.save()

        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        # article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        # article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, article_id):
        user = request.user.id
        article = get_object_or_404(Article, id=article_id)
        # article = Article.objects.get(id=article_id)
        
        if article.user.id == user:
            article.delete()
            return Response({"message": "삭제완료."}, status=status.HTTP_200_OK)
        
        else :
            return Response({"message": "권한이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    pass
# Create your views here.
