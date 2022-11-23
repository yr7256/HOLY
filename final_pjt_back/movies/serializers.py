from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

# 전체 영화


class MovieSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Genre
            fields = '__all__'

            
    like_movie_users_count = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = '__all__'


# 배우의 상세 정보
class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


# 감독의 상세 정보
class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'


# 장르
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


# class ProviderSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Provider
#         fields = '__all__'


class MovieLikeSerialzer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)

    like_movie_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'like_movie_users', )
