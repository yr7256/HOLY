from rest_framework import serializers
from .models import *


# 장르
# class GenreSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Genre
#         fields = '__all__'
#         read_only_fields = ('name',)

# 전체 영화


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

# 영화의 배우 리스트
# class ActorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actorlist
#         fields = '__all__'
#         read_only_fields = ('name', 'profile_path', 'character')

# 영화의 감독 리스트
# class DirectorListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Director
#         fields = '__all__'
        # read_only_fields = ('name', 'profile_path', 'job')

# 배우의 상세 정보
# class ActorDetailSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = '__all__'
#         read_only_fields = ('name', 'biography', 'profile_path')

# 감독의 상세 정보
# class DirectorDetailSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Director
#         fields = '__all__'
#         read_only_fields = ('name', 'biography', 'profile_path')

# 배우의 영화 정보
# class ActorMovieListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actormovie
#         fields = '__all__'
#         read_only_fields = ('overview', 'poster_path', 'release_date', 'title', 'character')

# 감독의 영화 정보
# class DirectorMovieListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Directormovie
#         fields = '__all__'
#         read_only_fields = ('overview', 'poster_path', 'release_date', 'title', 'job')
