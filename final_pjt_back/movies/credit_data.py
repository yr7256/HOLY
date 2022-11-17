import requests
import json

TMDB_API_KEY = '5ef064e7f4721766a54899e612e85f67'


# https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=ko-KR

def get_credit_datas():
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
            # print(movie)
            if movie.get('id', ''):
                # print(movie)
                movie_id = movie['id']
                request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_credit = requests.get(request_url).json()
                for credit in movie_credit['cast']:
                    if credit.get('known_for_department', '') == "Acting" and not credit.get('department', ''):
                        fields = {
                            'actor_id': credit['id'],
                            'department' : credit['known_for_department'],
                            'name': credit['name'],
                            'popularity': credit['popularity'],
                            'profile_path': credit['profile_path'],
                            'character': credit['character'],
                        }
                        # print(1)

                        data = {
                            "pk": movie['id'],
                            "model": "credits.movie",
                            "fields": fields
                        }

                        total_data.append(data)

    with open("credit_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_credit_datas()