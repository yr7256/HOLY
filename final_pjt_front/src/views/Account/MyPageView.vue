<template>
  <div class="body">
    <h1>User Profile</h1>
    <p>{{ $route.params.id }}</p>
    <h2>좋아요 한 영화</h2>
    <!-- <p>{{ userinfo.like_movies }}</p> -->
    <div class="row">
      <div class="col-2" v-for="(movie, index) in userinfo.like_movies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <!-- <div class="card" v-if="index <=11"> -->
          <div class="card">
            <img class="card-img-top" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
            <p class="card-text">{{ movie.title }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
// import userInfo from '@/components/Accounts/userInfo.vue'
// import favoriteMovie from '@/components/Accounts/favoriteMovie.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyPageView',
  components: {

  },
  data() {
    return {
      userinfo: null,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
    
  },
  computed: {

  },
  created() {
    this.getUserid()
  },
  methods: {
    getUserid() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          axios({
            method: 'get',
            url: `${API_URL}/accounts/${res.data.pk}/list/`,
            headers: {
              Authorization: `Token ${ this.$store.state.token }`
            }
          })
            .then((res) => {
              this.userinfo = res.data
              console.log(res)
            })
            .catch(err => console.log(err))          
            })
        .catch(err => console.log(err))
    },
  }
}


</script>

<style>
.body {
  padding-top: 75px;
  /* 생략 */
}
</style>