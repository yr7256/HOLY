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
                
                actor_request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                actor_list = requests.get(actor_request_url).json()
                for actor in actor_list['cast']:
                    if (actor.get('known_for_department', '') == "Acting" and not actor.get('department', '')):
                        if actor.get('id', ''):
                            actor_id = actor['id']
                            request_url = f"https://api.themoviedb.org/3/person/{actor_id}/movie_credits?api_key={TMDB_API_KEY}&language=en-US"
                          
                            movie_list = requests.get(request_url).json()
                            for movielist in movie_list['cast']:
                            
                                fields = {
                                    'movie_id': movielist['id'],
                                    'overview': movielist['overview'],
                                    'popularity':  movielist['popularity'],
                                    'poster_path': movielist['poster_path'],
                                    'release_date': movielist['release_date'],
                                    'title': movielist['title'],
                                    'character': movielist['character']
                                }
                                
                                data = {
                                    "pk": movie['id'],
                                    "model": "movies.actormovie",
                                    "fields": fields
                                }

                                total_data.append(data)
        


    with open("actor_movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

    

get_director_datas()