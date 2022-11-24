<template>
  <div class="w-75 mx-auto">
    <br>
    <h1 class="text-center" style="font-weight: bold">Now Playing</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, index) in sortnewmovies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <!-- <div class="card" v-if="index <=11"> -->
          <!-- <div class="card"> -->
            <!-- <figure class="snip1384">
                <img :src="MoviePosterurl+`${movie.poster_path}`" alt="">
                <figcaption>  
                  <p>{{ movie.title }}</p>
                </figcaption>
            </figure> -->
          <div class="card item-border">
            <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
          </div>
        </router-link>
      </div>
    </div>
    <br>
    <h1 class="text-center" style="font-weight: bold">Movies</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, index) in movies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <div class="card item-border">
            <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
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
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      message: null
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
      this.$store.dispatch('getNewMovies')
      this.$store.dispatch('getMovies')
    },
    methods: {
      mouseover: function() {
        // this.message = movie.title
      },
      // mousel
    }

  }
}

</script>

<style>

</style>