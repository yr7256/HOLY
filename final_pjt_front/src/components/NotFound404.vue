<template>
  <div class="bg404">
    <!-- <h1 class="page">404 Not Found</h1> -->
    <div class="container bg404">
      <router-link :to="{ name: 'MovieView' }">
        <img src="@/assets/404.png" alt="" class="img404">
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound404',
}
</script>

<style>
.bg404 {
  margin-top: 7rem;
  background-color: #1B1717;
}
.img404 {
  justify-content: center;
}
</style>