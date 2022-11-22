from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article, Comment
from articles.serializers import ArticleSerializer, ArticleCreateSerializer, CommentSerializer, CommentCreateSerializer


# 아티클 조회/등록 (임시)
# class ArticleView(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request):
#         articles = Article.objects.all().order_by("-pk")
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = ArticleCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# 좋아요 등록/취소
class LikeView(APIView):
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            article.likes.add(request.user)
            return Response("좋아요!", status=status.HTTP_200_OK)
        

# 북마크 등록/취소
class BookmarkView(APIView):
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.bookmarks.all():
            article.bookmarks.remove(request.user)
            return Response("북마크 취소", status=status.HTTP_200_OK)
        else:
            article.bookmarks.add(request.user)
            return Response("북마크 등록", status=status.HTTP_200_OK)