<template>
  <div>
    <h1>게시판</h1>
    <ArticleList/>
    <router-link :to="{ name: 'CreateView' }">글쓰기</router-link>
  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
      this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView' })
      }
    },
  }
}
</script>

<style>

</style>