from django.db import models
# from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True, blank=True)

class Director(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True, blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    vote_avg = models.FloatField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    video_url = models.CharField(max_length=200, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)


