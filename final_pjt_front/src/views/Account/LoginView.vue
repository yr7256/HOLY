<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">Username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> Password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="로그인">
      <!-- <GoogleLogin/> -->
     
    </form>
  </div>
</template>


<script>
// import GoogleLogin from '@/components/GoogleLogin.vue'

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  components: {
    // GoogleLogin
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('logIn', payload)
    },
  },
}

</script>

