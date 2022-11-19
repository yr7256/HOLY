import requests
import json

TMDB_API_KEY = '5ef064e7f4721766a54899e612e85f67'

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지의 데이터를 가져옴.
    for i in range(1, 5):
        # request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                # Movie 모델 필드명에 맞추어 데이터를 저장함.
                fields = {
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': -movie['popularity']*movie['vote_count'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'actors': [],
                    'directors': [],
                }

                data = {
                    "model": "movies.movie",
                    "pk": movie['id'],
                    "fields": fields
                }

                total_data.append(data)
    
    actor_datas = []
    director_datas = []

    for temp in total_data: # total data에서 영화 하나씩 뽑을거임
        people = f"https://api.themoviedb.org/3/movie/{temp['pk']}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
        people_list = requests.get(people).json()
        for actor in people_list['cast']:
            if actor['order'] < 10:
                temp['fields']['actors'].append(actor['id'])
                actor_fields = {
                    'name': actor['name'],
                    'profile_path': actor['profile_path']
                }

                actor_data = {
                    "model": "movies.actor",
                    "pk": actor['id'],
                    "fields": actor_fields
                }

                actor_datas.append(actor_data)


        for director in people_list.get('crew', ''):
            if director['job']=='Director' and director['department']== 'Directing':
                temp['fields']['directors'].append(director['id'])
                director_fields = {
                    'name': director['name'],
                    'profile_path': director['profile_path']
                }

                director_data = {
                    "model": "movies.director",
                    "pk": director['id'],
                    "fields": director_fields
                }

                director_datas.append(director_data)
        
    total_data += actor_datas
    total_data += director_datas

    genre_datas = []

    genre_url=f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genre_data = requests.get(genre_url).json()
    for genres in genre_data['genres']:
        fields = {
            'name': genres['name'],
        }

        genre_data = {
            "model": "movies.genre",
            "pk": genres['id'],
            "fields": fields
        }

        genre_datas.append(genre_data)
        total_data += genre_datas

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_movie_datas()

'''
actor=f'https://api.themoviedb.org/3/movie/{data['pk']}/credits?api_key={TMDB_API_KEY}&language=ko-KR'
["known_for_department"]=="Acting" and 


data['fields']['actors'].append('pk')
'''