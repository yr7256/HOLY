<template>
  <div class="page">
    <div class="container bgcontain32" style="color: #37383A">
      <h1 class="h1place" style="color: #37383A" >커뮤니티</h1>
      <ArticleList/>
      <button @click="getCreate" class="custom-btn btn-1" style="color: #37383A">글쓰기</button>
    </div>
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
.btn-margin2 {
  margin-left: 46.8% !important;
}

.bgcontain32 {
  margin-top: 5rem;
  background-color: #F2EFE8 ;
  background: linear-gradient(110deg, #F2EFE8 82%, rgba(0,0,0,0) 25%), url(@/assets/aud.PNG);
  /* background: 
  linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 59%, rgba(0, 0, 0, 0.65) 100%),
  url(@/assets/movie.png)no-repeat; */
  padding: 30px 60px  !important;
  /* border: solid 5px; */
  box-shadow: 0 6px 6px 0px #37383A;
  /* margin-bottom: 10rem; */
  border-radius: 0px 0px  0px;

}
</style>