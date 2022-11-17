import requests
import json

TMDB_API_KEY = '5ef064e7f4721766a54899e612e85f67'


# https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=ko-KR

def get_actor_datas():
    total_data = []

    # 1페이지부터 500페이지까지
    for i in range(1, 2):
        movie_request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        res = requests.get(movie_request_url)
        movies = res.json()
        cnt = 0
        # print(movies)
        # print(movies['total_results'])
        # print(movies['total_pages'])
        for movie in movies['results']:
            # print(movie['id'])
            # print(movie)
            if movie.get('id', ''):
                # print(movie)
                movie_id = movie['id']
                request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                actor_list = requests.get(request_url).json()
                for actor in actor_list['cast']:
                    if (actor.get('known_for_department', '') == "Acting" and not actor.get('department', '')):
                        fields = {
                            'actor_id': actor['id'],
                            'known_for_department' : actor['known_for_department'],
                            'name': actor['name'],
                            'popularity': actor['popularity'],
                            'profile_path': actor['profile_path'],
                            'character': actor['character'],
                        }
                        
                        data = {
                            "pk": movie['id'],
                            "model": "movies.actor",
                            "fields": fields
                        }
                        
                        cnt += 1

                        if cnt > 20:
                            break
                        else:
                            total_data.append(data)
                        
    


    with open("actor_list_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

    

get_actor_datas()