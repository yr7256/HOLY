<template>
  <div class="w-75 mx-auto">
    <br>
    <h1 class="text-center">Now Playing</h1>
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
    <h1 class="text-center">Movies</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, $index) in movies" :key="$index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <div class="card item-border">
            <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
          </div>
        </router-link>
      </div>
      <infinite-loading @infinite="infiniteHandler"></infinite-loading>
    </div>
  </div>
</template>

<script>
import _ from "lodash"
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieList',
  data() {
    return {
      // movies: this.$store.state.movies,
      newmovies: this.$store.state.newmovies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      message: null,
      page: 1,
      movies: [],
    }
  },
  computed: {
    sortnewmovies() {
      return _.sortBy(this.newmovies, 'popularity')
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getNewMovies')
      // this.$store.dispatch('getMovies')
    },
    infiniteHandler($state) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/pagination/`,
        params: {
          page: this.page,
        }
      }).then(({ data }) => {
          if (data.results?.length) {
            this.page += 1;
            this.movies.push(...data.results);
            $state.loaded();
          } else {
            $state.complete();
          }
        });
    },
  }
}


</script>

<style>

</style>