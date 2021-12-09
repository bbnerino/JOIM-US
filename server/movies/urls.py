from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    path('', views.main_page),
    path('api-token-auth/', obtain_jwt_token),
    path('selectmovies/', views.select_movies),
    path('get_actors/<int:movie_pk>/', views.get_actor),
    path('<int:movie_pk>/', views.detail_movie),
    path('<int:user_pk>/getrecommendedmovies/', views.get_recommended_movies),
]
