<template>
  <div class="w-75 mx-auto">
    <br>
    <br>
    <br>
    <br>
    <h1 class="text-center" style="color: #F2EFE8">마음에 드는 영화나 포스터를 골라주세요</h1>
    <br>
    <div class="row movie-list">
      <div class="col-3 movie-item gy-3" v-for="(movie, index) in movies" :key="index">
        <!-- <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }"> -->
          <div class="card item-border" @click="PickMovie(movie.id)">
            <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
          </div>
        <!-- </router-link> -->
      </div>
    </div>
  </div>
</template>

<script>
// import _ from "lodash"
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";


export default {
  name: 'MovieList',
  data() {
    return {
      movies: this.$store.state.movies,
      // newmovies: this.$store.state.newmovies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      // message: null
    }
  },
  computed: {
    // sortnewmovies() {
    //   return _.sortBy(this.newmovies, -'popularity')
    // },
    // isLike() {
    //   return _.includes(this.movie.like_movie_users, this.$store.state.userid)
    // }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      // this.$store.dispatch('getNewMovies')
      this.$store.dispatch('getMovies')
    },
    methods: {
      mouseover: function() {
        // this.message = movie.title
      },
      // mousel
    },
    PickMovie(data) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${data}/like/`,
        data: {
        },
        headers: {
          Authorization: `Token ${this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res.data.like_movie_users)
          // console.log(this.heart)
          // console.log(this.$store.state.userid)
          // location.reload();
        })
        .catch(err => console.log(err))
    } 
  },

  }


</script>

<style>

</style>