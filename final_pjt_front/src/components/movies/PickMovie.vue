<template>
  <div class="w-75 mx-auto">
    <br>
    <br>
    <br>
    <br>
    <h1 class="text-center" style="color: #F2EFE8">마음에 드는 영화나 포스터를 골라주세요</h1>
    <br>
    <router-link :to="{ name: 'MyPageView' }"><button class="custom-btn2 btn-1 size2" style="color: #F2EFE8 ">선택완료</button></router-link>
    <div class="row movie-list">
      <div class="col-3 movie-item gy-3" v-for="(movie, index) in movies" :key="index" @click="selectMovie(index)">
        <div v-if="selectedMovieArr && selectedMovieArr.includes(index)" style="text-align: center;">이 영화가 선택되었어요</div> 
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
.custom-btn2 {
  width: 130px;
  height: 40px;
  padding: 0px;
  border: 2px solid #151515 !important;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  text-align: top;
  color: #F2EFE8;
  margin-left: 550px;
}
.btn-1 {
  transition: all 0.3s ease;
}
.btn-1:hover {
  box-shadow:
  -7px -7px 20px 0px #fff9,
  -4px -4px 5px 0px #fff9,
  7px 7px 20px 0px #0002,
  4px 4px 5px 0px #0001;
}
</style>