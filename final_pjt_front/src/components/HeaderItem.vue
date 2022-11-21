<template>
  <div>
    <div id="head" v-if="isLogin" > 
      <nav class="d-flex head">
        <div class="">
          <router-link :to="{ name: 'MovieView' }">메인</router-link> |
          <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link>
        </div>
        <div class="flex-grow-1 text-end">
          <div>
            <input v-model="searchInput" @keypress.enter="getResult" type="text">
            <button @click="getResult" style="color:white;">Search</button>
            <!-- <searchListItem/> -->
          </div>
        </div>
        <div class="">
          <router-link :to="{ name: 'MyPageView', params: { id: $store.state.username} }">마이페이지</router-link> |
          <router-link @click.native="logout" :to="{ name: 'LoginView' }">로그아웃</router-link>
        </div>
      </nav>
      <router-view/>
    </div>
    <div id="head" v-else>
      <nav class="d-flex head">
        <div class="col">
          <router-link :to="{ name: 'MovieView' }">메인</router-link> |
          <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link>
        </div>
        <div class="col-2 text-end">
          <router-link :to="{ name: 'LoginView' }">로그인</router-link> |
          <router-link :to="{ name: 'SignUpView' }">회원가입</router-link>
        </div>
      </nav>
      <router-view/>
    </div>
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
      const options = {
        params: {
          q: this.searchInput,
        }
      }
      axios.get(API_URL + '/movies/search/', options)
        .then(res => {
          this.resultMovies = res.data
          console.log(res.data)
        })
        .catch(err => console.error(err.response.data))
    },
  
  },
}
</script>

<style>

</style>

