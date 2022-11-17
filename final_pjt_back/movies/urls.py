from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_detail),
]
