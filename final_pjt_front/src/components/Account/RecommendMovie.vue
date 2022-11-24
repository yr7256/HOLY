<template>
  <div>
    <img :src="MoviePosterurl+`${recommendMovie.poster_path}`" alt="">
  </div>
</template>

<script>
export default {
  name: 'RecommendMovie',
  props: {
    recommendMovie: Object
  },
  data() {
    return {
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
    }
  },
  computed: {

  },

  methods: {

  }
}
</script>

<style>

</style>