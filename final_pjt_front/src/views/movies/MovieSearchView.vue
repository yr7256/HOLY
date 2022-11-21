<template>
  <div>
    <h1 class="body">검색하신 영화는 다음과 같습니다.</h1>
    <div class="row">
      <div class="col-2" v-for="(movie, index) in $store.state.resultMovies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <div class="card">
            <img class="" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
            <p class="">{{ movie.title }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieSearchView',
  data() {
    return {
      resultMovies: this.$store.state.resultMovies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
  },
}
</script>

<style>
.body {
  padding-top: 60px;
}
</style>