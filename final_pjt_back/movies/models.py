from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
         return self.name

class Actorlist(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    known_for_department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    popularity = models.FloatField(null=True, blank=True)
    profile_path = models.CharField(max_length=200, null=True, blank=True)
    character = models.CharField(max_length=100)

class Directorlist(models.Model):
    director_id = models.IntegerField(primary_key=True)
    known_for_department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    popularity = models.FloatField(null=True, blank=True)
    profile_path = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    vote_avg = models.FloatField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    video_url = models.CharField(max_length=200, null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    # actors = models.ManyToManyField(Actorlist)
    # director = 
    like_movie_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    wish_lists_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_moives', blank=True)
    rates_users = models.ManyToManyField('accounts.User', related_name='user_rated_movie', through='Rate')

    def __str__(self):
        return self.title


class Rate(models.Model):
    rate_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_rated')
    rate_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate_score = models.FloatField()



class Actor(models.Model):
    actor_id = models.ManyToManyField(Actorlist, related_name='actor_movies')
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    profile_path = models.CharField(max_length=200, null=True, blank=True)

class Director(models.Model):
    director_id = models.ManyToManyField(Directorlist, related_name='director_movies')
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    profile_path = models.CharField(max_length=200, null=True, blank=True)

class Actormovie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    overview = models.TextField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100)
    character = models.CharField(max_length=100)

class Directormovie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    overview = models.TextField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

