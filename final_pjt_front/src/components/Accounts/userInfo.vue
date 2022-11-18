<template>
  <div>
    <nav class="col-4">
      <h1>User info</h1>
      <br>
      <h1>Favorites</h1>
    </nav>
    <nav class="userInfo">
      {{ $store.state.username }}
    </nav>
    

  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'userInfo',
  data: function () {
    return {
      
    }   
  },
  // methods: {
  //   getInfo() {
  //     this.username = sessionStorage.getItem('username')
  //     const token = sessionStorage.getItem('jwt')
  //     // const user_id = jwtDecode(token).user_id
  //     const options = {
  //       headers: {
  //         Authorization: `JWT ${token}`
  //       }
  //     }
  //     axios.get(API_URL+'/accounts/', options)
  //   }
  // }, 

    
}

</script>

<style>

</style>