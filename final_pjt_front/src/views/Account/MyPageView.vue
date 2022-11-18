<template>
  <div>
    <h1>User Profile</h1>
    <userInfo/>

  </div>
</template>

<script>
import userInfo from '@/components/Accounts/userInfo.vue'

export default {
  name: 'MyPageView',
  components: {
    userInfo

  },
  data: function () {
    return {

    }
    
  },
  computed: {

  },
  created : function(){
    this.loginCheck()
  }, 
  methods: {
    loginCheck : function(){
      if (!this.$store.state.token){
        const detailItem ={
          name: 'MypageView',
          params: this.$route.params.username
        }
        this.$store.dispatch('getArticles', detailItem)
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name : 'LoginView'})
      }
    }
  },

 

}


</script>

<style>

</style>