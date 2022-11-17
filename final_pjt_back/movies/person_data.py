import requests
import json

TMDB_API_KEY = '5ef064e7f4721766a54899e612e85f67'


# https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=ko-KR

def get_credit_datas():
    total_data = []

    # 1페이지부터 500페이지까지 
    for i in range(1, 501):
        movie_request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        res =  requests.get( movie_request_url)
        movies = res.json()

        for movie in movies['results']:
            if movie.get('popularity', ''):
                movie_id = movie['id']
                credit_request_url = f" https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
                movie_credit = requests.get(credit_request_url)
                credits = movie_credit.json()

                for credit in credits['results']:
                    if credit.get('', ''):
                        person_id = credit['id']
                        person_request_url = f"https://api.themoviedb.org/3/person/{person_id}?api_key={TMDB_API_KEY}&language=en-US"
                        person_data = requests.get(person_request_url)
                        print(person_data)
                
                        fields = {
                            'actor_id': movie['id'],
                            'known_for_department' : movie['known_for_department'],
                            'name': movie['name'],
                            'popularity': movie['popularity'],
                            'profile_path': movie['profile_path'],
                            'character': movie['character'],
                        }

                        data = {
                            "pk": movie['id'],
                            "model": "credits.movie",
                            "fields": fields
                        }

                        total_data.append(data)

    with open("person_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_credit_datas()

