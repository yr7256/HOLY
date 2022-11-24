<template>
  <div class="w-75 mx-auto">
    <br>
    <br>
    <br>
    <br>
    <h1 class="text-center" style="color: #F2EFE8">마음에 드는 영화나 포스터를 골라주세요</h1>
    <br>
    <div class="row movie-list">
      <div class="col-3 movie-item gy-3" v-for="(movie, index) in movies" :key="index" @click="selectMovie(index)">
        <div v-if="selectedMovieArr && selectedMovieArr.includes(index)">이영화가 선택되었어요</div> 
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
import _ from "lodash"
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";


export default {
  name: 'MovieList',
  data() {
    return {
      movies: this.$store.state.movies,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      selectedMovieArr:[9999],
    }
  },
  computed: {
    isLike() {
      return _.includes(this.movie.like_movie_users, this.$store.state.userid)
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    selectMovie(index){
      const newselectedMovieArr = this.selectedMovieArr.slice()
      if(this.selectedMovieArr.includes(index)){
        newselectedMovieArr.splice(newselectedMovieArr.indexOf(index),1)
        this.selectedMovieArr =  newselectedMovieArr
      }else{
      const changeArr = this.selectedMovieArr.slice()
      changeArr.push(index)
      this.selectedMovieArr = changeArr
      }
    },
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
        })
        .catch(err => console.log(err))
    } 
  },

  }


</script>

<style>

</style>