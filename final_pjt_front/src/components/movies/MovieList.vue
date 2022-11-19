<template>
  <div class="w-75 mx-auto">
    <h1 class="text-center">Now Playing</h1>
    <div class="row">
      <div class="col-2" v-for="(movie, index) in sortmovies" :key="index">
        <div class="card" v-if="index <=11">
          <img class="card-img-top" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
          <p class="card-text">{{ movie.title }}</p>
        </div>
      </div>
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