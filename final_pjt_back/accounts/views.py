from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import *
from django.http import JsonResponse
from .serializers import *
from movies.models import *
from movies.serializers import *
from django.db.models import Count

# Create your views here.
User = get_user_model()
movies = Movie.objects.annotate(
    like_movie_users_count=Count('like_movie_users', distinct=True))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_movie_list(request, user_pk):
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    user_list = {
        'id': serializer.data.get('id'),
        'like_movies': serializer.data.get('like_movies'),
    }
    return JsonResponse(user_list)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_algorithm_recommend(request, user_pk):
    movie_list = movies.filter().order_by('popularity')[:30]
    genre = Genre.objects.all()
    serializer = MovieSerializer(movie_list, many=True)
    
    # return JsonResponse(serializer.data, safe=False)
