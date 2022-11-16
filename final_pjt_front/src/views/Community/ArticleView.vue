<template>
  <div>
    <h1>게시판</h1>
    <router-link :to="{ name: 'CreateView' }">글쓰기</router-link>
  </div>
</template>

<script>
export default {
  name: 'ArticleView',
  components: {

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
      this.$store.dispatch('getArticles')
      }
    }
  }
</script>

<style>

</style>