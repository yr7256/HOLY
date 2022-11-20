from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_pk>/list/', views.user_movie_list),
]