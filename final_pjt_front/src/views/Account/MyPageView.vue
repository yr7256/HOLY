<template>
  <div class="page">
    <!-- <div id="box"> -->
      <div class ="profile">
        <!-- <span class="bod"> -->
          <div class="container bgcontain1"  style="padding: 10px">
            <!-- <div class="box namecontain"> -->

            
            <h1 style="color: #37383A" class="pad">{{ $route.params.id }}'s COLLECTION</h1>
            <hr class="my-hr">
            <!-- </div> -->
            <!-- <p></p> -->
            <!-- <div class="box" style="background: #BDBDBD;">
              <img class="profile1" src="@/assets/profile.png">
            </div> -->
            <br>
            <h3 style="color:#37383A" class="pad1" >YOUR FAVORITE MOVIE</h3>
            <br>
            <!-- <div class="row movie-list"> -->
            <swiper :options="swiperOption">
              <SwiperSlide v-for="(movie, index) in userinfo.like_movies" :key="index">
                <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                  <div class="card card-border-none" style="background-color: #F2EFE8">
                    <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="" >
                    <!-- <p>{{ movie.title }}</p> -->
                  </div>
                </router-link>
              <!-- </div> -->
              </SwiperSlide>
            </swiper>
            <br>
            <br>
            <h3 style="color:#37383A" class="pad1" >HOLY RECOMMEND MOVIE</h3>
            <br>
            
            <!-- <div v-for="(movie, index) in recommendMovie" :key="index">
              <p>{{movie.title}}</p>
            </div> -->
            <!-- <p>{{ recommendMovies }}</p> -->
            <swiper :options="swiperOption">
              <SwiperSlide v-for="(movie, index) in recommendMovies" :key="index">
                <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                  <div class="card card-border-none" style="background-color: #F2EFE8">
                    <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="">
                  </div>
                </router-link>
              </SwiperSlide>
            </swiper>
            <!-- <img :src="MoviePosterurl+`${recommendMovie.poster_path}`" alt=""> -->
            <!-- <swiper :options="swiperOption"> -->
            <!-- <RecommendMovie 
      v-for="recommendMovie in recommendMovies"
      :key="recommendMovie.id"
      :recommendMovie="recommendMovie"
    /> -->
  
  
      </div>
    </div>
  </div>
  <!-- </div> -->
</template>

<script>
import axios from 'axios'
import { Swiper, SwiperSlide  } from "vue-awesome-swiper";
import "swiper/css/swiper.css";
// import RecommendMovie from "@/components/Account/RecommendMovie"

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'MyPageView',
  components: {
    Swiper,
    SwiperSlide,
    // RecommendMovie
  },
  data() {
    return {
      userinfo: null,
      MoviePosterurl: 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2',
      swiperOption: { 
        slidesPerView: 5, 
        spaceBetween: 30, 
        loop: false, 
        pagination: { 
            el: '.swiper-pagination', 
            clickable: true 
        }, 
        navigation: { 
            nextEl: '.swiper-button-next', 
            prevEl: '.swiper-button-prev' 
        },
        recommendMovies: null 
      },
    };
  },
  computed: {
    recommendMovies() {
      return this.$store.state.recommendMovies
    }
  },
  created() {
    this.getUserid()
    this.getRecommendMovies()
  },
  methods: {
    getUserid() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          axios({
            method: 'get',
            url: `${API_URL}/accounts/${res.data.pk}/list/`,
            headers: {
              Authorization: `Token ${ this.$store.state.token }`
            }
          })
            .then((res) => {
              this.userinfo = res.data
              console.log(res)
            })
            .catch(err => console.log(err))          
            })
        .catch(err => console.log(err))
    },
    getRecommendMovies() {
      this.$store.dispatch('getRecommendMovies')
    },
  }
}


</script>

<style>

.profile {
  /* background-color: linear-gradient(#37383A 50%, #F2EFE8 50%); */
  position: relative;
  z-index: 1;
  background-size: cover;
  width: 100%;
  height: 100%;
  border: 4px;
  border-color: white ;
  border-radius: 25px;
  }

.bgcontain1 {
  margin-top: 5rem;
  /* background-image: #F2EFE8 ; */
  padding: 30px 60px !important;
  background-color:  #F2EFE8 !important;
  padding: 60px;
  /* border: solid 5px; */
  box-shadow: 0 6px 6px 0px #37383A;
  /* margin-bottom: 10rem; */
  border-radius: 0px 0px  0px;

}
/* .fontcolor {
  font-color:#37383A
} */
.wh {
  height: 260px;
  width: 200px;
  
}
.pad {
  padding: auto;
  font-weight: bold;
  font-size:2cm;
  
}
.pad1 {
  padding: auto;
  font-weight: bold;
  /* font-size:2cm; */
  
}
.box {
  width: 150px;
  height: 150px; 
  border-radius: 70%;
  overflow: hidden;
  margin-left: 35em;
  border-color: #37383A !important;
  background-color: #F2EFE8 !important;
}
.profile1 {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background-color: #F2EFE8 !important;
  justify-content: center;
}
.my-hr {
    border: 0;
    height: 2px;
    background: #080808;
  }
.card-border-none {
  border-style: none !important;
}
</style>
