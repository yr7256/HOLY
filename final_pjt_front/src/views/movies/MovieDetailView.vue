<template>
  <div class="page">
    <div class="container contain">
      <!-- <div class="card bg-black mb-3 mt-2"> -->
        <div class="row g-0">
          <div class="col-md-4">
            <img :src="MoviePosterurl + `${movie?.poster_path}`" @error="noPosterImg"/>
          </div>
          <div class="col-md-8 mt-4">
            <div class="card-body mt-5" style="text-align:left;">
              <h1>{{ movie?.title }}</h1>
              <h4>{{ movie?.release_date }}</h4>
              <form action="" style="text-align: left;">
                <span @click="LikeMovie" v-if="isheart">
                  <img src="@/assets/fullheart.png" alt="" style="width: 20px">
                </span>
                <span style="color: #ea4335" @click="LikeMovie" v-else>
                  <img src="@/assets/emptyheart.png" alt="" style="width: 20px">
                </span>
              </form>
              <br> 
              <p class = "overview">{{movie?.overview}}</p>
            <br>
            <a :href="wavveUrl + `${movie?.title}`" style="margin-right: 10px">
              <img src="@/assets/wavve.jpg" alt="" style="width: 70px ;">
            </a>
            <a :href="seeznUrl + `${movie?.title}`" style="margin-right: 10px">
              <img src="@/assets/seezn.jpg" alt="" style="width: 65px">
            </a>
            <!-- <a :href="appletvUrl + `${movie?.title}`" >
              <img src="@/assets/appletv.jpg" alt="" style="width: 68px ;">
            </a> -->
          </div>
        </div>
      </div>
    <br>
    <br>
    <div class="container contain">
      <br>
      <h3 class="me-5">감독</h3>
        <div class="row movie-list">
          <div class="contain col-2 movie-item gy-3 mx-auto" v-for="(name, index) in directors" :key="index">
              <a class :href="personDetailurl + `${name.id}`">
                <figure class="snip1384" >
                  <img class="card-img-top" :src="MoviePosterurl+`${name.profile_path}`" alt="" @error="noDirectorImg">
                  <figcaption>
                  <p>{{ name.name }}</p>
                </figcaption>
                </figure>
              </a>
          </div>
        </div>
      </div>
      
    
    <div class="container contain">

      <h3 class="me-5">출연</h3>
        <div class="row movie-list">
          <div class="col-2 movie-item gy-2 mx-auto" v-for="(name, index) in actors" :key="index">
              <a :href="personDetailurl + `${name.id}`">
                <figure class="snip1384" >
                  <img class="card-img" :src="MoviePosterurl+`${name.profile_path}`" alt="" @error="noImage">
                <figcaption>
                  <p>{{ name.name }}</p>
                </figcaption>
                </figure>
              </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import img from '@/assets/actorimg.png'
import directorimg from '@/assets/directorimg.png'
import posterimg from '@/assets/noposterimg.png'
import _ from "lodash"

export default {
  name: "MovieDetailView",
  data() {
    return {
      movie: null,
      MoviePosterurl: "https://www.themoviedb.org/t/p/w300_and_h450_bestv2",
      actors: [],
      actorsLength: 0,
      personDetailurl: "https://www.themoviedb.org/person/",
      directors: [],
      wavveUrl: "https://www.wavve.com/search?searchWord=",
      seeznUrl: "https://www.seezntv.com/search?category_id=all&sort=AC&keywords=",
      // appleUrl: "https://tv.apple.com/search?term=",
      // hasuser: true
      heart : true
    };
  },
  created() {
    this.getActorList();
    this.getDirectorList();
  },
  computed: {
    isheart() {
      return _.includes(this.movie.like_movie_users, this.$store.state.userid)
    }
  },
  components: {
    
  },
  methods: {
    getActorList() {
      axios({
        methods: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/`,
      })
        .then((res) => {
          console.log(res);
          this.movie = res.data;
          const actorArr = res.data.actors;
          this.actorsLength = actorArr.length;
          for (let i = 0; i < actorArr.length; i++) {
            axios({
              methods: "get",
              url: `${API_URL}/movies/actors/${actorArr[i]}/`,
            })
              .then((response) => {
                this.actors.push(response.data);
              })
              .catch((err) => console.log(err));
          }
        })
      },
    getDirectorList() {
      axios({
        methods: "get",
        url: `${API_URL}/movies/${this.$route.params.id}/`,
      })
        .then((res) => {
          console.log(res);
          this.movie = res.data;
          const directorArr = res.data.directors;
          this.directorsLength = directorArr.length;
          for (let i = 0; i < directorArr.length; i++) {
            axios({
              methods: "get",
              url: `${API_URL}/movies/directors/${directorArr[i]}/`,
            })
              .then((response) => {
                this.directors.push(response.data);
              })
              .catch((err) => console.log(err));
            }
          })  
        },
      noImage(e) {
        e.target.src = img
      },
      noDirectorImg(e) {
        e.target.src = directorimg
      },
      noPosterImg(e) {
        e.target.src = posterimg
      },
      LikeMovie() {
        axios({
          method: 'post',
          url: `${API_URL}/movies/${this.$route.params.id}/like/`,
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
            location.reload();
          })
          .catch(err => console.log(err))
      } 
  },
}

</script>

<style>
.contain {
  background-color: #151515;
}
img {
  /* float:left */
  margin-top: 2px;
  justify-content: center;
}
.overview {
  word-break: keep-all;
  word-wrap: break-word;

}


h3 {
  margin-top: 5px;
}
figure.snip1384 {
  font-family: 'Raleway', Arial, sans-serif;
  position: relative;
  overflow: hidden;
  /* margin: 10px; */
  min-width: 140px;
  max-width: 240px;
  width: 50%;
  color: white;
  text-align: left;
  font-size: 14px;
  vertical-align: middle;
  word-break: normal;
  /* margin-right: 20px; */
  
  /* background-color: #000000; */
}
figure.snip1384 * {
  -webkit-box-sizing: border-box;
  box-sizing: content-box;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
}
figure.snip1384 img {
  max-width: 140px;
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
  background-color: transparent !important;
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
  opacity: 1;
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