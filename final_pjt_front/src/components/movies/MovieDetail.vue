<template>
  <div>
    <h1>{{ movie?.title }}</h1>
    <img :src="MoviePosterurl+`${movie.poster_path}`" alt="">
  </div>

</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'MovieDetail',
  data() {
    return {
      movies: this.$store.state.movies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'

    }
  },
  methods: {
    getMovieDetail() {
      axios({
        methods: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/`
      })
        .then((res) => {
          console.log(res)
          
        })
    }
  }
 }
</script>

<style>

</style>