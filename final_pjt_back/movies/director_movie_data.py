import requests
import json

TMDB_API_KEY = '5ef064e7f4721766a54899e612e85f67'


def get_director_datas():
    total_data = []

    for i in range(1, 2):
        movie_request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        res = requests.get(movie_request_url)
        movies = res.json()

        for movie in movies['results']:
            if movie.get('id', ''):
                movie_id = movie['id']

                director_request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                director_list = requests.get(director_request_url).json()
                for director in director_list['crew']:
                    if director.get('job', '') == 'Director' and director.get('department', '') == 'Directing':
                        if director.get('id', ''):
                            director_id = director['id']
                
                            request_url = f"https://api.themoviedb.org/3/person/{director_id}/movie_credits?api_key={TMDB_API_KEY}&language=en-US"
                          
                            movie_list = requests.get(request_url).json()
                            for movielist in movie_list['crew']:
                            
                                fields = {
                                    'movie_id': movielist['id'],
                                    'overview': movielist['overview'],
                                    'popularity':  movielist['popularity'],
                                    'poster_path': movielist['poster_path'],
                                    'release_date': movielist['release_date'],
                                    'title': movielist['title'],
                                    'department': movielist['department'],
                                    'job': movielist['job']
                                }
                                
                                data = {
                                    "pk": movie['id'],
                                    "model": "movies.directormovie",
                                    "fields": fields
                                }

                                total_data.append(data)
        


    with open("director_movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

    

get_director_datas()