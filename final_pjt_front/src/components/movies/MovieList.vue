<template>
  <div>
    <h1>무비리스트</h1>
    
  </div>
</template>

<script>
export default {
  name: 'MovieList',
  data() {
    return {
      movies: this.$store.state.movies
    }
  }
}

</script>

<style>

</style>