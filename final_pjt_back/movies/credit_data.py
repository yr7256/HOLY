import requests
import json

TMDB_API_KEY = '5ef064e7f4721766a54899e612e85f67'


# https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=ko-KR

def get_credit_datas():
    total_data = []

    # 1페이지부터 500페이지까지 
    for i in range(1, 2):
        movie_request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        res =  requests.get(movie_request_url)
        movies = res.json()

        # print(movies['total_results'])
        # print(movies['total_pages'])
        for movie in movies['results']:
            print(movie['id'])
            if movie.get('name', ''):
                movie_id = movie['id']
                request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_credit = requests.get(request_url).json()
                print(movie_credit)
                
                if movie_credit.get('known_for_department', '') == "Acting":
                    fields = {
                        'actor_id': movie['id'],
                        'known_for_department' : movie['known_for_department'],
                        'name': movie['name'],
                        'popularity': movie['popularity'],
                        'profile_path': movie['profile_path'],
                        'character': movie['character'],
                    }
                    # print(1)

                    # data = {
                    #     "pk": movie['id'],
                    #     "model": "credits.movie",
                    #     "fields": fields
                    # }

                    # total_data.append(data)

    # with open("credit_data.json", "w", encoding="utf-8") as w:
    #     json.dump(total_data, w, indent="\t", ensure_ascii=False)

# get_credit_datas()

