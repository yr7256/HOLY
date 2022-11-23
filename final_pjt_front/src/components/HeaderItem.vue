<template>
  <div id="head" v-if="isLogin"> 
    <nav class="head navbar navbar-expand-lg">
      <div class="container-fluid">
        <span class="navbar-brand ms-5">
          <router-link :to="{ name: 'MovieView' }">
            <img src="@/assets/navlogo.png" alt="" class="mx-auto logo">
          </router-link>
        </span>
        <span class="navbar-brand ms-2">        
          <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link>
        </span>
        
        <div class="d-flex justify-content-end flex-grow-1">
          <input class="form-control me-5 w-25" v-model="searchInput" @keypress.enter="getResult" placeholder="Search" aria-label="Search">
          <!-- <button @click="getResult" style="color:white;">Search</button> -->
        </div>
        <span class="navbar-brand me-4">
          <router-link :to="{ name: 'MyPageView', params: { id: $store.state.username} }">마이페이지</router-link>
        </span>
        <span class="navbar-brand me-5">
          <router-link @click.native="logout" :to="{ name: 'LoginView' }">로그아웃</router-link>
        </span>
      </div>
    </nav>
    <router-view/>
  </div>
  <div id="head" v-else>
    <nav class="d-flex head navbar navbar-expand-lg">
      <div class="container-fluid">
        <span class="navbar-brand ms-5">
          <router-link :to="{ name: 'MovieView' }">
            <img src="@/assets/navlogo.png" alt="" class="mx-auto logo">
          </router-link>
        </span>
        <span class="navbar-brand ms-2">
          <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link>
        </span>
        <div class="d-flex justify-content-end flex-grow-1">
          <input class="form-control me-5 w-25" v-model="searchInput" @keypress.enter="getResult" placeholder="Search" aria-label="Search">
          <!-- <button @click="getResult" class="btn btn-light">Search</button> -->
        </div>
        <span class="navbar-brand me-5">
          <router-link :to="{ name: 'LoginView' }">회원가입/로그인</router-link>
        </span>
        <!-- <span class="navbar-brand">
          <router-link :to="{ name: 'SignUpView' }">회원가입</router-link>
        </span> -->
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
// import searchListItem from '@/movies/searchListItem.vue'

export default {
  name: 'HeaderItem',
  data () {
    return {
      searchInput: '',
      resultMovies: [],
    }
  },
  components: {
    // searchListItem

  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
    getResult() {
      this.$store.dispatch('getResult')
      const options = {
        params: {
          q: this.searchInput,
        }
      }
      axios.get(API_URL + '/movies/search/', options)
        .then(res => {
          this.$store.state.resultMovies = res.data
          console.log(res.data)
          this.$router.push({name: 'MovieSearchView'})
        })
        .catch(err => console.error(err.response.data))
    },
  },

}
</script>

<style>
.logo {
  width: 72px;
  text-align: center;

}


</style>

