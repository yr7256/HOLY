from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('new/', views.new_movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('directors/', views.director_list),
    path('directors/<int:director_pk>/', views.director_detail),
    path('<int:movie_pk>/like/', views.movie_like),
    path('search/', views.MovieListPaginate.as_view()),
]
