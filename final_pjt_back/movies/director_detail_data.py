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
                
                director_request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                director_list = requests.get(director_request_url).json()
                for director in director_list['crew']:
                    if director.get('job', '') == 'Director' and director.get('department', '') == 'Directing':
                        if director.get('id', ''):
                            person_id = director['id']
                            
                            request_url = f"https://api.themoviedb.org/3/person/{person_id}?api_key={TMDB_API_KEY}&language=us-US"
                            director_detail = requests.get(request_url).json()

                            fields = {
                                'director_id': director_detail['id'],
                                'name': director_detail['name'],
                                'biography': director_detail['biography'],
                                'profile_path': director_detail['profile_path']
                            }
                            
                            data = {
                                "pk": movie['id'],
                                "model": "movies.director",
                                "fields": fields
                            }

                            total_data.append(data)
        


    with open("director_detail_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

    

get_director_datas()