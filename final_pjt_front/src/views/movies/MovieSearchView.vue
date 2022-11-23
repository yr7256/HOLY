<template>
  <div>
    <div class="container contain5 ">
      <h1 class="page">{{this.$store.state.username}}님의 검색 결과는 다음과 같습니다.</h1>
        <div class="row movie-list2">
          <swiper :options="swiperOption">
              <SwiperSlide class="col-2 movie-item gy-3" v-for="(movie, index) in $store.state.resultMovies" :key="index">
                <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                  <div class="card item-border">
                    <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
                    <!-- <p class="">{{ movie.title }}</p> -->
                  </div>
                </router-link>
              </SwiperSlide>
          </swiper>
          <!-- </div> -->
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import posterimg from '@/assets/noposterimg.png'
import { Swiper, SwiperSlide  } from "vue-awesome-swiper";
import "swiper/css/swiper.css";


export default {
  name: 'MovieSearchView',
  components: {
    Swiper,
    SwiperSlide

  },
  data() {
    return {
      // movie: null,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      MovieDetailPage: 'http://localhost:8080/movies/',
      swiperOption: { 
        slidesPerView: 4, 
        spaceBetween: 35, 
        loop: false, 
        pagination: { 
            el: '.swiper-pagination', 
            clickable: true 
        }, 
        navigation: { 
            nextEl: '.swiper-button-next', 
            prevEl: '.swiper-button-prev' 
        } 
      },
    };

    },
  
  created() {
    this.searchMovie()

  },
  methods: {
    searchMovie() {
      axios({
        methods: "get",
        url: `${API_URL}/movies/search/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.movie = res.data
          console.log(res)
          
        })
        .catch(err => console.log(err))  
    },
    noPosterImg(e) {
        e.target.src = posterimg
      },

  }
}
</script>

<style>
.contain5 {
  background-color: #151515;
  margin-top: 5rem;
}
.movie-list2 {
  margin-top: 5rem !important;
}

</style>