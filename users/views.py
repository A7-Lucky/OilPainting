from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import ProfileSerializer

# Create your views here.
class ProfileView(APIView):
    def get(self, request):
        user = request.user
        profile = user.user_profile.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
