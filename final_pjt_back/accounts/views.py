from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import *
from django.http import JsonResponse
from .serializers import *
from movies.models import *
from movies.serializers import *
from django.db.models import Count
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Create your views here.
User = get_user_model()
movies = Movie.objects.annotate(
    like_movie_users_count=Count('like_movie_users', distinct=True))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_movie_list(request, user_pk):
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    user_list = {
        'id': serializer.data.get('id'),
        'like_movies': serializer.data.get('like_movies'),
    }
    return JsonResponse(user_list)


@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_algorithm_recommend(request, user_pk):
    # 콘텐츠 기반 추천 : 사용자가 특정 아이템을 선호하는 경우 그 아이템과 비슷한 콘텐츠를 가진 다른 아이템을 추천해주는 방식
    
    # 1. json 데이터 추출하고 장르 id를 name으로 변경
    movies_json = open('./movies/fixtures/movie_data.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    gerne_json = open('./movies/genres.json', encoding='UTF8')
    gerne_list = json.load(gerne_json)


    for num in range(len(movies_list)): # 전체 데이터 중 
        if movies_list[num]['model'] == 'movies.movie': # 영화에 해당하는 데이터에서
            data = movies_list[num]['fields'] # 각 필드에서
            for j in range(len(data['genres'])): # 장르 리스트를 확인하고
                for k in range(len(gerne_list)): # 장르의 id를 name으로 변경
                    if data['genres'][j] == gerne_list[k].get('pk'):
                        data['genres'][j] = gerne_list[k].get('name')



    # 2. 데이터 프레임 형태로 변환 : 1739개
    data = movies_list[0]['fields']
    movie_df= pd.DataFrame([data])
    for num in range(1, len(movies_list)):
        if movies_list[num]['model'] == 'movies.movie':
            movie_df_plus= pd.DataFrame([movies_list[num]['fields']])
            movie_df = pd.concat([movie_df, movie_df_plus])
    

    # 가중 평균(wr) : 많은 사람들이 좋은 평점을 준 영화를 찾기 위해 선택(m보다 v가 높아야 의미있는 데이터)
    # wr = (v/(v+m))*R + (m/(v+m))*C
    # v : 개별 영화의 투표 수, m : 평점을 부여하기 위한(순위안에 들어야 하는) 최소 투표 횟수(정하기 나름)
    # R : 개별 영화에 대한 평점, C : 전체 영화에 대한 평균 평점

    # 3. 평점을 부여하기 위한 최소 투표 횟수(m) 구하기
    m = movie_df['vote_count'].quantile(0.6) # 상위 n%에 들기 위해서는 최소 m을 넘어야 하며
    # movie_df = movie_df.loc[movie_df['vote_count'] >= m]
    

    # 4. 전체 영화에 대한 평균 평점(C) 구하기
    C = movie_df['vote_average'].mean() # C : 6.632317423806786
    

    # 5. 최종 추천 점수를 계산할 함수
    def weighted_rating(x, m = m, C = C):
        v = x['vote_count'] # 평점 투표 수
        R = x['vote_average'] # 평점
        return ((v/(v+m))*R)+((m/(m+v))*C) # 반환값 : wr(가중 평균)


    # 6. 최종 추천 점수를 movie_df에 score라는 컬럼(axis=1)으로 추가
    movie_df['score'] = movie_df.apply(weighted_rating, axis=1)

    # 7. 최종 데이터 수 확인
    # print(movie_df.shape)

    # 8. 데이터 전처리 : 공백 문자로 word 단위가 구분되는 문자열로 변환
    movie_df['genres'] = movie_df['genres'].apply(lambda x: " ".join(x))

    
    # 9. 전처리한 데이터를 TF-IDF 방법을 이용해 벡터화
    tfidf_vector = TfidfVectorizer(ngram_range=(1,2))
    tfidf_matrix = tfidf_vector.fit_transform(movie_df['genres']).toarray()

    # 10. tf-idf vector를 코사인 유사도를 활용해서 유사도 값을 구함
    cosine_sim = cosine_similarity(tfidf_matrix)
    # 코사인 유사도를 구한 matrix
    cosine_sim_df = pd.DataFrame(cosine_sim, index = movie_df.title, columns = movie_df.title)
    

    # 11. 특정 영화(사용자가 좋아요/평점을 높게 준 영화)와 유사한 영화를 추천해주는 함수
    # 추천 결과를 조회할 영화 제목, 코사인 유사도를 구한 matrix, 영화 데이터
    
    def genre_recommendations(target_title, matrix, items, k=10):
        # 특정 영화의 정보를 추출하여 유사한 코사인 유사도를 가진 정보를 추출
        # 코사인 유사도 중 영화 제목 인덱스에 해당하는 값에서 추천 개수만큼 추출
        recom_idx = matrix.loc[:, target_title].values.reshape(1, -1).argsort()[:, ::-1].flatten()[1:k+1]
        recom_id = items.iloc[recom_idx, :].movie_id.values 
        recom_title = items.iloc[recom_idx, :].title.values
        recom_genre = items.iloc[recom_idx, :].genres.values
        overview = items.iloc[recom_idx, :].overview.values
        poster_path = items.iloc[recom_idx, :].poster_path.values
        popularity = items.iloc[recom_idx, :].popularity.values
        release_date = items.iloc[recom_idx, :].release_date.values
        score = items.iloc[recom_idx, :].score.values

        result = {
            'id' : recom_id,
            'title' : recom_title,
            'genre' : recom_genre,
            'overview' : overview,
            'poster_path' : poster_path,
            'popularity' : popularity,
            'release_date' : release_date,
            'score' : score
        }
        return pd.DataFrame(result)

    # =================================== #
    # 사용자가 좋아요한 영화 중, 랜덤으로 1개 선택 #  
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    like_lst = serializer.data.get('like_movies') # 리스트
    if like_lst: # 좋아요한 영화가 있는 경우
        random_list = []
        for i in range(len(like_lst)):
            random_list.append(like_lst[i].get('title'))
        pick_movie = random.choice(random_list)
    else: # 좋아요한 영화가 없는 경우
        pick_movie = Movie.objects.values('title').order_by('?').first().get('title')
    # =================================== #

    reco = genre_recommendations(pick_movie, cosine_sim_df, movie_df)

    result = []
    for l in range(10):
        result.append(
            {
                'id' : int(reco.iloc[l]['id']),
                'title' : reco.iloc[l]['title'],
                'genre' : reco.iloc[l]['genre'],
                'release_date' : reco.iloc[l]['release_date'],
                'poster_path' : reco.iloc[l]['poster_path'],
                'overview' : reco.iloc[l]['overview'],
                'score' : reco.iloc[l]['score'],
            }
        )
    # safe : 전송데이터가 딕셔너리가 아니거나, 
    # 딕셔너리 이외의 객체를 직렬화하려면 False로 설정해야함(기본값 : True)
    return JsonResponse(result, safe=False)