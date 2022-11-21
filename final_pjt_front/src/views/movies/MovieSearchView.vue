<template>
  <h1 class="body">검색하신 영화는 다음과 같습니다.</h1>
  <!-- <p>{{ }}</p> -->
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieSearchView',
  data() {
    return {
      // movie: null,
      // MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
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
          // this.movie = res.data
          console.log(res)
        })
        .catch(err => console.log(err))  
    }
  }
  

}
</script>

<style>
.body {
  padding-top: 75px;
  /* 생략 */
}

</style>