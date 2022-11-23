from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_pk>/list/', views.user_movie_list),
    path('<int:user_pk>/recommend/', views.user_algorithm_recommend),
]