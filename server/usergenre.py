from bs4 import BeautifulSoup
import urllib.request
import pprint
import json
import sqlite3

conn = sqlite3.connect("db.sqlite3", isolation_level=None)

c = conn.cursor()

c.execute("select * from accounts_user;")
genre_list = ['adventure', 'fantasy', 'animation', 'drama', 'horror', 'action', 'comedy', 'historic', 'western', 'thriller', 'criminal', 'documentary', 'sf', 'mystery', 'music', 'romance', 'family', 'millitary', 'tv']
# print(c.fetchone())
users = c.fetchall()
for i in range(len(users)):
    # print(users[i])
    user_id = users[i][0]
    c.execute('select actor_id from accounts_user_like_actors where user_id=%d;' % (user_id))
    user_actors = c.fetchall()
    # print(user_actors)
    for j in range(len(user_actors)):
        for k in range(len(user_actors[j])):
            # print(user_actors[j][k])
            one = user_actors[j][k]
            c.execute("select adventure, fantasy, animation, drama, horror, action, comedy, historic, western, thriller, criminal, documentary, sf, mystery, music, romance, family, millitary, tv from movies_actor where actor_id = %d;" % (one))
            new_score = c.fetchone()
            for l in range(len(genre_list)):
                if new_score[l]:
                    c.execute("update accounts_user_genre_score set %s=%s + %d where user_id = %d;" % (genre_list[l], genre_list[l], new_score[l], user_id))

    # movie_id = movies[i][10]
    # movie_just_id = movies[i][0]
    # movie_name = movies[i][1]
    # # print(movie_id)
    # c.execute("select * from movies_movie_genres where movie_id = %d;" % (movie_just_id,))
    # movie_genres = c.fetchall()
    # # print(movie_genres)
    # url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8c060ba9a7cd2b8cbddbebf2d3d0cb8a'
    # req = urllib.request.Request(url)
    # html = urllib.request.urlopen(req).read()
    # S = json.loads(html.decode('utf-8'))

    # for j in range(len(S["cast"])):
    #     if S["cast"][j]["popularity"] >= 10:
    #         c.execute('in