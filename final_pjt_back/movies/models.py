from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True, blank=True)

class Director(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True, blank=True)

# class Provider(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    trim_title = models.CharField(max_length=100)
    trim_original_title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    video_url = models.CharField(max_length=200, null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    like_movie_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    # providers = models.ManyToManyField(Provider, blank=True)
