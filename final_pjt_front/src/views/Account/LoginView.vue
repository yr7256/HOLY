<template>
  <!-- <div class="body">
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">Username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> Password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="로그인">
     
    </form>
  </div> -->
<div class="padding mt-5">
  <div class="cont page">
    <form class="form sign-in" @submit.prevent="logIn">
      <h2 class="h2tag1">Welcome back</h2>
      <label>
        <span class="h2tag1">username</span>
        <input type="text" v-model="username"/>
      </label>
      <br>
      <label>
        <span class="h2tag1">Password</span>
        <input type="password" v-model="password"/>
      </label>
      <button type="submit" class="submit btn-margin">Login</button>
    </form>
    <div class="sub-cont">
      <div class="img">
      <div class="img__text m--up">
        <h2 class="whitetag">New here?</h2>
        <p>Sign up and discover great amount of new opportunities!</p>
      </div>
      <div class="img__text m--in">
        <h2 class="whitetag">One of us?</h2>
        <p>If you already has an account, just sign in. We've missed you!</p>
      </div>
      <div class="img__btn" @click="toggleForm">
        <span class="m--up">회원가입</span>
        <span class="m--in">로그인</span>
      </div>
    </div>
    <form class="form sign-up" @submit.prevent="signUp">
      <h2 class="h2tag1 h2pad">Time to feel like CINEMA</h2>
      <label>
        <span class="h2tag1">Username</span>
        <input type="text" v-model="username"/>
      </label>
      <br>
      <label>
        <span class="h2tag1">password</span>
        <input type="password" v-model="password1"/>
      </label>
      <br>
      <label>
        <span class="h2tag1">password confirmation</span>
        <input type="password" v-model="password2"/>
      </label>
      <button type="submit" class="submit btn-margin">Sign Up</button>
    </form>
  </div>
  </div>
</div>
</template>


<script>

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      // username2: null,
      password1: null,
      password2: null,
    }
  },
  components: {
    
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
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    },
    toggleForm() {
      const cont = document.querySelector('.cont');
      cont.classList.toggle('s--signup');
    }
  },
}

</script>

<style>
/* @import url(@/assets/css/login.scss); */
.padding {
  padding: 100px !important;
}
form {
  text-align: center;
}
.btn-margin {
  margin-left: 160px !important;
}
.h2tag1 {
  font-weight: bold;
  color: #37383A;
}
.whitetag {
  color: #F2EFE8 
}
.h2pad {
  padding-top: 30px
}
</style>

