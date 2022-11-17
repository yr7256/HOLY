<template>
  <!-- <div id="app">
    <nav>
      <router-link :to="{ name: 'MovieView' }">메인</router-link> |
      <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link> |
      <router-link :to="{ name: 'LoginView' }">로그인</router-link> |
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link>
    </nav>
    <router-view/>
  </div> --> 
  <HeaderItem/>
</template>
<script>
import HeaderItem from '@/components/HeaderItem.vue'

export default ({
  components: {
    HeaderItem
  },
})
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #2c3e50;
}
</style>
