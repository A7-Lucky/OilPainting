from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article, Comment
from articles.serializers import ArticleSerializer, ArticleCreateSerializer, CommentSerializer, CommentCreateSerializer
from users.serializers import UserSerializer


# 아티클 조회/등록(테스트용)
class ArticleView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        articles = Article.objects.all().order_by("-pk")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# 아티클 디테일 조회
class ArticleDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
# 아티클 유저 정보
class ArticleUserView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        user = article.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 댓글 조회/등록
class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        comments = article.comment_article.all().order_by("-pk")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, article_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article_id=article_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 댓글 수정/삭제
class CommentDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentCreateSerializer(comment, data=request.data)
        if request.user == comment.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)


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


# 나의 북마크 리스트
class MybookmarkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        bookmarks = user.article_bookmarks.all()
        serializer = ArticleSerializer(bookmarks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 나의 아티클 리스트
class MyarticleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        articles = user.article_set.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


