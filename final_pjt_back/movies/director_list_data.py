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

        # print(movies)
        # print(movies['total_results'])
        # print(movies['total_pages'])
        for movie in movies['results']:
            # print(movie['id'])
            
            if movie.get('id', ''):
                # print(movie)
                movie_id = movie['id']
                
                request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                director_list = requests.get(request_url).json()
                for director in director_list['crew']:
                    if director.get('job', '') == 'Director' and director.get('department', '') == 'Directing':
                        fields = {
                            'director_id': director['id'],
                            'known_for_department' : director['known_for_department'],
                            'name':director['name'],
                            'popularity': director['popularity'],
                            'profile_path': director['profile_path'],
                            'department' : director['department'],
                            'job' : director['job']
                        }
                        
                        data = {
                            "pk": movie['id'],
                            "model": "movies.director",
                            "fields": fields
                        }

                        total_data.append(data)
        


    with open("director_list_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

    

get_director_datas()