<template>
  <div>
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
</style>