import json
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .serializers import MovieSerializer
from .models import Actor, Genre, Movie

import sqlite3
import random

# Create your views here.
@api_view(['GET'])
def main_page(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def get_actor(request, movie_pk):
    conn = sqlite3.connect("db.sqlite3", isolation_level=None)
    c = conn.cursor()
    c.execute("select iden from movies_movie where id=%d;" % (movie_pk))
    movie_id = c.fetchone()
    c.execute("select actor_id from movies_appear_actor where movie_id=%d;" % (movie_id))

    movies = c.fetchall()
    appear_actors = [{'actor_id': 0, 'name': '', 'profile_path':'',} for _ in range(len(movies))]
    # print(movies)
    # print(appear_actors)
    for i in range(len(movies)):
        # print(movies[i][0])
        movies[i][0]
        c.execute("select actor_id, name, profile_path from movies_actor where actor_id=%d;" % (movies[i][0]))
        new = c.fetchone()
        appear_actors[i]['actor_id'] = new[0]
        appear_actors[i]['name'] = new[1]
        appear_actors[i]['profile_path'] = new[2]
        
    # print(new)
    # print(new[1])

    # print(appear_actors)

    return Response(appear_actors)

@api_view(['GET'])
def get_recommended_movies(request, user_pk):
    genre_list = ['adventure', 'fantasy', 'animation', 'drama', 'horror', 'action', 'comedy', 'historic', 'western', 'thriller', 'criminal', 'documentary', 'sf', 'mystery', 'music', 'romance', 'family', 'millitary', 'tv']
    genre_dict = {'adventure':0, 'fantasy':0, 'animation':0, 'drama':0, 'horror':0, 'action':0, 'comedy':0, 'historic':0, 'western':0, 'thriller':0, 'criminal':0, 'documentary':0, 'sf':0, 'mystery':0, 'music':0, 'romance':0, 'family':0, 'millitary':0, 'tv':0}
    genre_names = {'adventure':'모험', 'fantasy':'판타지', 'animation':'애니메이션', 'drama':'드라마', 'horror':'공포', 'action':'액션', 'comedy':'코미디', 'historic':'역사', 'western':'서부', 'thriller':'스릴러', 'criminal':'범죄', 'documentary':'다큐멘터리', 'sf':'SF', 'mystery':'미스터리', 'music':'음악', 'romance':'로맨스', 'family':'가족', 'millitary':'전쟁', 'tv':'TV 영화'}
 
    genre_score = [0] * len(genre_list)
    conn = sqlite3.connect("db.sqlite3", isolation_level=None)
    c = conn.cursor()
    c.execute("select * from accounts_user_genre_score where user_id=%d;" % (user_pk))
    my_score = c.fetchone()
    for i in range(1, len(my_score)):
        genre_score[i-1] = my_score[i]
        genre_dict[genre_list[i-1]] = my_score[i]
    if max(genre_score) == 0 or sorted(genre_score, reverse=True)[1] == 0:
        # return Response([{'one': 1}, {'two': 1}])
        return Response([{'one': None}, {'two': None}])
    most_liked_genre = sorted(genre_dict.items(), key=lambda x:x[1], reverse=True)[0][0]
    second_liked_genre = sorted(genre_dict.items(), key=lambda x:x[1], reverse=True)[1][0]
    # print(most_liked_genre)
    # print(second_liked_genre)
    genre_name = genre_names[most_liked_genre]
    genre_name_two = genre_names[second_liked_genre]

    genre = Genre.objects.get(name=genre_name)
    genre_two = Genre.objects.get(name=genre_name_two)

    movies = Movie.objects.filter(genres=genre.id)
    movies_two = Movie.objects.filter(genres=genre_two.id)

    one = sorted(movies.values('id', 'title', 'vote_average', 'poster_path'), key=lambda x: x['vote_average'], reverse=True)
    two = sorted(movies_two.values('id', 'title', 'vote_average', 'poster_path'), key=lambda x: x['vote_average'], reverse=True)

    # 여기부터는 10개 미만일때, 오류를 막기 위한
    l_one = min(10, len(one))
    l_two = min(10, len(two))

    one_ran = random.sample(one, l_one)
    two_ran = random.sample(two, l_two)
    
    i = 0
    while len(one_ran)<10:
        one_ran.append(one_ran[i])
        i+=1
    j=0
    while len(two_ran)<10:
        two_ran.append(two_ran[j])
        j+=1
    # print(one_ran)
    # print(two_ran)
    recommend_movies = [{'one': one_ran}, {'two': two_ran}, {'one_genre': genre_name}, {'two_genre': genre_name_two}]
    
    return Response(recommend_movies)

@api_view(['POST'])
def select_movies(request):
    select_type = request.data.get('select_type')
    find_word = request.data.get('find_word')
    # print(select_type, find_word)
    new = []
    if select_type == 'movie_name':
        movies = Movie.objects.filter(title__contains=find_word)
        new = MovieSerializer(movies, many=True).data
        # print(new)
    else:
        conn = sqlite3.connect("db.sqlite3", isolation_level=None)
        c = conn.cursor()
        c.execute("select * from movies_appear_actor where actor_name like '%%%s%%';" % (find_word,))
        a_movies = c.fetchall()
        # print(a_movies)
        # new = []
        for i in range(len(a_movies)):
            # print(a_movies[i][1])
            # print(Movie.objects.get(iden=a_movies[i][1]))
            new.append(MovieSerializer(Movie.objects.get(iden=a_movies[i][1])).data)

        # print(new)
    return Response(new)