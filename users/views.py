from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer
from django.contrib.auth import logout


# 회원가입 (임시)
# class UserView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         user = request.user
#         user.delete()
#         return Response({"message": "회원 탈퇴 완료!"}, status=status.HTTP_200_OK)
