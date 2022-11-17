<template>
  <div id="head" v-if="isLogin">
    <h3>{{ $store.state.username }}</h3>
    <nav>
      <router-link :to="{ name: 'MovieView' }">메인</router-link> |
      <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link> |
      <router-link @click.native="logout" :to="{ name: 'LoginView' }">로그아웃</router-link>
    </nav>
    <router-view/>
  </div>
  <div id="head" v-else>
    <nav>
      <router-link :to="{ name: 'MovieView' }">메인</router-link> |
      <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link> |
      <router-link :to="{ name: 'LoginView' }">로그인</router-link> |
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'HeaderItem',
  data () {
    return {

    }
  },
  components: {

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
    getUser() {
      this.$store.dispatch('getUser')
    },
  },
  created() {
    this.getUser()
  }
}
</script>

<style>

</style>