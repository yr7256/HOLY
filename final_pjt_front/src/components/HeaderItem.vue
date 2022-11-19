<template>
  <div>
    <div id="head" v-if="isLogin" > 
      <nav class="header">
        
        <h3>{{ $store.state.username }}님 안녕하세요!</h3>
        <router-link :to="{ name: 'MovieView' }">메인</router-link> |
        <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link> |
        <router-link :to="{ name: 'MyPageView' }">마이페이지</router-link> |
        <router-link @click.native="logout" :to="{ name: 'LoginView' }">로그아웃</router-link>
      </nav>
      <router-view/>
    </div>
    <div id="head" v-else>
      <nav class="header">
        <span>MENU</span>
        <router-link :to="{ name: 'MovieView' }">메인</router-link> |
        <router-link :to="{ name: 'ArticleView' }">커뮤니티</router-link> |
        <router-link :to="{ name: 'LoginView' }">로그인</router-link> |
        <router-link :to="{ name: 'SignUpView' }">회원가입</router-link>
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

.header {
  position: fixed;
  /* animation: down 0.5s ease; */
  top: 0;
  /* width: 100%; */
  left: 0;
  right: 0;
  height: 50px;
  padding: 1rem;
  color: #151515;
  background: #151515;
  font-weight: bold;
  display: flex;
  justify-content: space-around;
  align-items: center;
  transition: top 0.5s;
  box-shadow: 0px 1px 20px rgba(0, 0,0,0,2);
 
  
}

</style>

