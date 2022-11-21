<template>
  <div>
    <h1 class="body">검색하신 영화는 다음과 같습니다.</h1>
    <div v-for="(pk, index) in $store.state.resultMovies" :key="index" @error="noPosterImg">
      <a :href="MovieDetailPage + `${pk.id}`">
        <img :src="MoviePosterurl+`${pk.poster_path}`" alt="" >
      </a>
      <p>{{ pk.title }}</p>
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
  padding-top: 75px;
  /* 생략 */
}
.img {
  max-width: 100%;
  transition: all 0.2s linear;
}

</style>