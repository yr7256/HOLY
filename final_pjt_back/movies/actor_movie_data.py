import requests
import json

TMDB_API_KEY = '5ef064e7f4721766a54899e612e85f67'


# https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=ko-KR

def get_director_datas():
    total_data = []

    # 1페이지부터 500페이지까지
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
                            
                            requests.get(request_url).json
                            
                            fields = {
                                'movie_id': actor['id'],
                                'overview': actor['overview'],
                                'popularity':  actor['popularity'],
                                'profile_path': actor['profile_path'],
                                'released_date': actor['release_date'],
                                'title': actor['title'],
                                'character': actor['character']
                            }
                            
                            data = {
                                "pk": movie['id'],
                                "model": "movies.actormovie",
                                "fields": fields
                            }

                            total_data.append(data)
        


    # with open("actor_movie_data.json", "w", encoding="utf-8") as w:
    #     json.dump(total_data, w, indent="\t", ensure_ascii=False)

    

get_director_datas()