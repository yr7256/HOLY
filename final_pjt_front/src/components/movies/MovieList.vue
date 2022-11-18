<template>
  <div>
    <h1>무비리스트</h1>
    <div v-for="(movie, index) in movies" :key="index">
      <img :src="MoviePosterurl+`${movie.poster_path}`" alt="">
      {{ movie.title }}
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
  }
}

</script>

<style>

</style>