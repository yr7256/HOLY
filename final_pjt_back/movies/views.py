# from datetime import date
import datetime
from django.shortcuts import render
from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, APIView
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.permissions import *
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer, MovieLikeSerialzer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model

movies = Movie.objects.annotate(
    like_movie_users_count=Count('like_movie_users', distinct=True))


@api_view(['GET'])
def movie_list(request):
    # movies = Movie.objects.all()
    movie_list = movies.filter().order_by('popularity')[:30]
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def new_movie_list(request):
    new_movie = movies.filter(release_date__lte=(datetime.datetime.now(
    )-datetime.timedelta(days=3))).order_by('-release_date', 'popularity')[:12]
    serializer = MovieSerializer(new_movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_detail(request, movie_pk):
    movie = movies.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def director_list(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def director_detail(request, director_pk):
    director = Director.objects.get(pk=director_pk)
    serializer = DirectorSerializer(director)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_movie_users.filter(pk=user.pk).exists():
        movie.like_movie_users.remove(user)
    else:
        movie.like_movie_users.add(user)

    serializer = MovieLikeSerialzer(movie)

    like_movie_register = {
        'id': serializer.data.get('id'),
        'like_movie_users_count': movie.like_movie_users.count(),
        'like_movie_users': serializer.data.get('like_movie_users'),
    }
    return JsonResponse(like_movie_register)



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page'


class MovieListPaginate(APIView):

    def get(self, request):
        paginator = StandardResultsSetPagination()
        if request.GET.get('orderBy'):
            orderBy = request.GET.get('orderBy')
            movie = movies.order_by(orderBy)
        elif request.GET.get('q'):
            q = request.GET.get('q')
            movie = movies.filter(title__icontains=q) | movies.filter(original_title__icontains=q) | movies.filter(
                trim_title__icontains=q) | movies.filter(trim_original_title__icontains=q)
            serializer = MovieSerializer(movie, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "no result"})

        result_page = paginator.paginate_queryset(movie, request)
        serializer = MovieSerializer(result_page, many=True)
        return Response(serializer.data)
