<template>
  <div class="page">
    <div class ="profile" >
      <h1>{{ $route.params.id }}님의 페이지입니다.</h1>
      <!-- <p></p> -->
      <h2 style="color: white">좋아요 한 영화</h2>

      <div class="row movie-list">
        <div class="col-2 movie-item gy-3" v-for="(movie, index) in userinfo.like_movies" :key="index">
          <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
            <!-- <div class="card" v-if="index <=11"> -->
            <div class="card item-border">
              <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
              <!-- <p class="card-text">{{ movie.title }}</p> -->
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
.profile {
    position: relative;
    z-index: 1;
    background-size: cover;
    width: 100%;
    height: 100%;
  }
</style>