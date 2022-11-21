<template>
  <div class="h2">
    <span style="color: #ea4335" @click="likeMovie" v-if="!hasUser">
      <i class="far fa-heart"></i>
    </span>
    <span style="color: #ea4335" @click="likeMovie" v-else>
      <i class="fas fa-heart"></i>
    </span>

  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "LikeMovie",

}
</script>

<style>

</style>