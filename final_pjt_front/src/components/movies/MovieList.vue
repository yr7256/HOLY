<template>
  <div class="w-75 mx-auto">
    <h1 class="text-center">Best</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, index) in movies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <!-- <div class="card" v-if="index <=11"> -->
          <div class="">
            <img class="card-img-top" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
            <!-- <p class="card-text">{{ movie.title }}</p> -->
          </div>
        </router-link>
      </div>
    </div>
    <h1 class="text-center">Now Playing</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, index) in sortnewmovies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <div class="">
            <img class="card-img-top" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
            <!-- <p class="card-text">{{ movie.title }}</p> -->
          </div>
        </router-link>
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
      newmovies: this.$store.state.newmovies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
  },
  computed: {
    sortnewmovies() {
      return _.sortBy(this.newmovies, -'popularity')
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
      this.$store.dispatch('getNewMovies')
    },
    // goDetail() {
    //   this.$router.push({ name: 'MovieDetailView' })
    // }
  }
}

</script>

<style>

</style>