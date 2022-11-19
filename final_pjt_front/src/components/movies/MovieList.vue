<template>
  <div>
    <h1>Now Playing</h1>
    <div v-for="(movie, index) in movies" :key="index">
      <div v-if="index <=8">
        <div class="">
          <img :src="MoviePosterurl+`${movie.poster_path}`" alt="">
          {{ movie.title }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>

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