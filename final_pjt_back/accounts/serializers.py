from movies.models import Movie
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserMovieListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
