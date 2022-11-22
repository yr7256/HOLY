<template>
  <div class="w-75 mx-auto">
    <br>
    <h1 class="text-center">Now Playing</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, index) in sortnewmovies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <!-- <div class="card" v-if="index <=11"> -->
          <!-- <div class="card"> -->
            <!-- <figure class="snip1384">
                <img :src="MoviePosterurl+`${movie.poster_path}`" alt="">
                <figcaption>  
                  <p>{{ movie.title }}</p>
                </figcaption>
            </figure> -->
          <div class="card item-border">
            <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
            <!-- <p class="card-text">{{ movie.title }}</p> -->
          </div>
        </router-link>
      </div>
    </div>
    <br>
    <h1 class="text-center">Movies</h1>
    <div class="row movie-list">
      <div class="col-2 movie-item gy-3" v-for="(movie, index) in movies" :key="index">
        <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
          <!-- <div class="card" v-if="index <=11"> -->
          <div class="card item-border">
            <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
            <!-- <p class="card-text">{{ movie.title }}</p> -->
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import _ from "lodash"
// import "@/css/NotoSansKR.css";
// import "@/fonts/Roboto.css";


export default {
  name: 'MovieList',
  data() {
    return {
      movies: this.$store.state.movies,
      newmovies: this.$store.state.newmovies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      message: null
    }
  },
  computed: {
    sortnewmovies() {
      return _.sortBy(this.newmovies, -'popularity')
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getNewMovies')
      this.$store.dispatch('getMovies')
    },
    methods: {
      mouseover: function() {
        // this.message = movie.title
      },
      // mousel
    }

  }
}

</script>

<style>
@import url(http://fonts.googleapis.com/earlyaccess/notosanskr.css);
/* @import url(https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css); */
figure.snip1384 {
  font-family: 'Raleway', Arial, sans-serif;
  position: relative;
  overflow: hidden;
  /* margin: 10px; */
  min-width: 140px;
  max-width: 240px;
  width: 100%;
  color: white;
  text-align: left;
  font-size: 14px;
  vertical-align: middle;
  word-break: normal;
  
  /* background-color: #000000; */
}
figure.snip1384 * {
  -webkit-box-sizing: border-box;
  box-sizing: content-box;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
}
figure.snip1384 img {
  max-width: 160px;
  max-height: 240px;
  backface-visibility: hidden;
  vertical-align: middle;
}
figure.snip1384:after,
figure.snip1384 figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  /* word-break: keep-all; */
  /* white-space: normal !important; */
  text-overflow:clip;
}
figure.snip1384:after {
  max-width: 140px;
  max-height: 240px;
  content: '';
  background-color: rgba(0, 0, 0, 0.65);
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
  opacity: 0;
}
figure.snip1384 figcaption {
  max-width: 140px;
  max-height: 240px;
  z-index: 1;
  padding: 20px;

}
figure.snip1384 h4,
figure.snip1384 .links {
  width: 100%;
  margin: 5px 0;
  padding: 0;
}
figure.snip1384 p {
  font-size: 0.8em;
  font-weight: 300;
  line-height: 1.1em;
  /* font-weight: 700; */
  font-size: 1.2em;
  letter-spacing: 1px;
  text-transform: uppercase;
  opacity: 0;
  top: 50%;
  -webkit-transform: translateY(40px);
  transform: translateY(40px);
  word-break: normal;
  white-space: normal;
  text-align: left;
  
  font-family: 'Noto Sans KR', sans-serif;
}
/* figure.snip1384 p {
  font-size: 0.8em;
  font-weight: 300;
  letter-spacing: 1px;
  opacity: 0;
  top: 50%;
  -webkit-transform: translateY(40px);
  transform: translateY(40px);
  word-break: keep-all;
  white-space: normal;
  word-spacing: 30px;
} */
figure.snip1384 i {
  position: absolute;
  bottom: 10px;
  right: 10px;
  padding: 20px 25px;
  font-size: 34px;
  opacity: 0;
  -webkit-transform: translateX(-10px);
  transform: translateX(-10px);
}
figure.snip1384 a {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1;
}
figure.snip1384:hover img,
figure.snip1384.hover img {
  zoom: 1;
  filter: alpha(opacity=50);
  -webkit-opacity: 0.5;
  opacity: 0.5;
}
figure.snip1384:hover:after,
figure.snip1384.hover:after {
  /* opacity: 1; */
  position: absolute;
  /* top: 10px;
  bottom: 10px;
  left: 10px;
  right: 10px; */
}
figure.snip1384:hover h4,
figure.snip1384.hover h4,
figure.snip1384:hover p,
figure.snip1384.hover p,
figure.snip1384:hover i,
figure.snip1384.hover i {
  -webkit-transform: translate(0px, 0px);
  transform: translate(0px, 0px);
  opacity: 1;
}

</style>