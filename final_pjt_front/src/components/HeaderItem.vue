<template>
  <div>
    <div id="head" v-if="isLogin" > 
      <nav class="d-flex head">
        <div class="">
          <router-link :to="{ name: 'MovieView' }">메인</router-link> |
          <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link>
        </div>
        <div class="flex-grow-1 text-end">
          <h5>{{ $store.state.username }}님 안녕하세요!</h5>
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
  },
}
</script>

<style>

</style>

