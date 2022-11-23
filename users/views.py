from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import ProfileSerializer, ProfileUpdateSerializer, UserSerializer


# 테스트용 회원가입 View
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # .all() 사용 시 모든 유저 데이터를 받게되므로 .get() 형태로 사용
        profile = User.objects.get(id=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile = User.objects.get(id=request.user.id)
        serializer = ProfileUpdateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)