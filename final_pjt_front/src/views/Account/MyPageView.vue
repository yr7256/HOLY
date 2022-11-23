<template>
  <div class="page">
    <!-- <div id="box"> -->
      <div class ="profile" >
        <!-- <span class="bod"> -->
          <div class="container bgcontain">
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
                  <div class="card item " style="background-color: #F2EFE8">
                    <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt="" >
                    <!-- <p>{{ movie.title }}</p> -->
                  </div>
                </router-link>
              <!-- </div> -->
              </SwiperSlide>
            </swiper>
            <br>
            <br>
            <h3 style="color:#37383A" class="pad1" >KILLING YOUR TIME</h3>
            <br>
          </div>
            <!-- </div> -->
        <!-- <hr> -->
        <!-- <swiper :options="swiperOption">
          <SwiperSlide>
            <div
              v-for="(movie, index) in userinfo.like_movies" :key="index">
              <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                <img class="card-img" :src="MoviePosterurl+`${movie.poster_path}`" alt=""  style="color: #F2EFE8">
              </router-link>
            </div>
          </SwiperSlide>
        </swiper>  -->
      </div> 
    </div>
  <!-- </div> -->
</template>

<script>
import axios from 'axios'
import { Swiper, SwiperSlide  } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'MyPageView',
  components: {
    Swiper,
    SwiperSlide
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
        } 
      },
    };
  },
  computed: {

  },
  created() {
    this.getUserid()
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

.bgcontain {
  margin-top: 5rem;
  /* background-image: #F2EFE8 ; */
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
</style>
