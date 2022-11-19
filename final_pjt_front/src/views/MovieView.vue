<template>
  <div class='page'>
    <img class="full mt-auto" alt="" src="../assets/main.png">
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

</style>