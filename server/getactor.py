from bs4 import BeautifulSoup
import urllib.request
import pprint
import json
import sqlite3

conn = sqlite3.connect("db.sqlite3", isolation_level=None)

c = conn.cursor()

c.execute("select * from movies_movie;")

# print(c.fetchone())
movies = c.fetchall()
for i in range(len(movies)):
    movie_id = movies[i][10]
    movie_just_id = movies[i][0]
    movie_name = movies[i][1]
    # print(movie_id)
    c.execute("select * from movies_movie_genres where movie_id = %d;" % (movie_just_id,))
    movie_genres = c.fetchall()
    # print(movie_genres)
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8c060ba9a7cd2b8cbddbebf2d3d0cb8a'
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req).read()
    S = json.loads(html.decode('utf-8'))

    for j in range(len(S["cast"])):
        if S["cast"][j]["popularity"] >= 10:
            c.execute('insert into movies_appear_actor(movie_id, actor_id, movie_name, actor_name) values(%d, %d, "%s", "%s");' % (movie_id, S["cast"][j]["id"], movie_name, S["cast"][j]["name"]))
