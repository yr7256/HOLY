<template>
  <div>
    <h1 class="body">검색하신 영화는 다음과 같습니다.</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, index) in $store.state.resultMovies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <div class="card item-border">
            <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
            <!-- <p class="">{{ movie.title }}</p> -->
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import posterimg from '@/assets/noposterimg.png'


export default {
  name: 'MovieSearchView',
  data() {
    return {
      // movie: null,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      MovieDetailPage: 'http://localhost:8080/movies/'
    }
  },
  created() {
    this.searchMovie()

  },
  methods: {
    searchMovie() {
      axios({
        methods: "get",
        url: `${API_URL}/movies/search/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.movie = res.data
          console.log(res)
          
        })
        .catch(err => console.log(err))  
    },
    noPosterImg(e) {
        e.target.src = posterimg
      },

  }
}
</script>

<style>
.body {
  padding-top: 60px;
}
</style>