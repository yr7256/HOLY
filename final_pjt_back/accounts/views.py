from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import *
from django.http import JsonResponse
from .serializers import *

# Create your views here.
User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_movie_list(request, user_pk):
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    user_list = {
        'id' : serializer.data.get('id'),
        # 'like_movies_count' : Users.like_movies.count(),
        'like_movies' : serializer.data.get('like_movies'),
    }
    return JsonResponse(user_list)