<template>
  <div>
    <!-- <swiper :options="swiperOption"> -->
    <img :src="MoviePosterurl+`${recommendMovie.poster_path}`" alt="">
      <!-- </img> -->
    <!-- </swiper> -->
  </div>
</template>

<script>
// import { Swiper, SwiperSlide  } from "vue-awesome-swiper";
// import "swiper/css/swiper.css";

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
    // Swiper,
    // SwiperSlide,

  },

  methods: {

  }
}
</script>

<style>

</style>