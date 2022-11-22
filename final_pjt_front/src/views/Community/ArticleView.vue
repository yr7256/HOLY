<template>
  <div class="body">
    <h1>게시판</h1>
    <ArticleList/>
    <button @click="getCreate" class="btn-gradient yellow">글쓰기</button>
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
    },
    
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    },
    getCreate() {
      if (this.isLogin) {
      this.$router.push({ name: 'CreateView'})
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView' })
      }
    },
  }
}
</script>

<style>
.body {
  padding-top: 60px;
}
</style>