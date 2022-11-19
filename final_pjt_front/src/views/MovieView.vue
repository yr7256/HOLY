<template>
  <div class="body">
    <img class="full" alt="" src="../assets/main.png">
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList
  },
}
</script>

<style>
.full {
  width: 100vw;
}
.body {
  top:0;
  padding-top: 75px;
  /* 생략 */
}
</style>