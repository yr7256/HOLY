<template>
  <div>
    <h1>무비리스트</h1>
    <div v-for="(movie, index) in sortmovies" :key="index">
      <img :src="MoviePosterurl+`${movie.poster_path}`" alt="">
      {{ movie.title }}
    </div>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'MovieList',
  data() {
    return {
      movies: this.$store.state.movies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
  },
  computed: {
    movieurl() {
      return this.img_url+this.movie.poster_path
    },
    sortmovies() {
      return _.sortBy(this.movies,'popularity')
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
  }
}

</script>

<style>

</style>