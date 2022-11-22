<template>
  <div class="body">
    <h1>{{ movie?.title }}</h1>
    <img :src="MoviePosterurl + `${movie?.poster_path}`" @error="noPosterImg" />
    <p>{{ movie?.release_date }}</p>
    <hr>
    <form action="">
      <span @click="LikeMovie" v-if="isheart">
        <img src="@/assets/fullheart.png" alt="" style="width: 20px">
      </span>
      <span style="color: #ea4335" @click="LikeMovie" v-else>
        <img src="@/assets/emptyheart.png" alt="" style="width: 20px">
      </span>
    <!-- <button @click="LikeMovie">좋아요</button> -->
    </form>
    
    <hr>
    <h3>Directing</h3>
      <div class="row movie-list">
        <div class="col-1 movie-item gy-3" v-for="(name, index) in directors" :key="index">
          <div class="card">
            <a :href="personDetailurl + `${name.id}`">
              <img class="card-img-top" :src="MoviePosterurl+`${name.profile_path}`" alt="" @error="noDirectorImg">
            </a>
            <div class="card-body">
              <p class="card-title">{{ name.name }}</p>
            </div>
          </div>
        </div>
      </div>
    <br>
    <h3>Casting</h3>
      <div class="row movie-list">
        <div class="col-1 movie-item gy-3" v-for="(name, index) in actors" :key="index">
          <div class="card">
            <a :href="personDetailurl + `${name.id}`">
              <img class="card-img-top" :src="MoviePosterurl+`${name.profile_path}`" alt="" @error="noImage">
            </a>
            <div class="card-body">
              <p class="card-title">{{ name.name }}</p>
            </div>
          </div>
        </div>
      </div>
    

      <!-- <div v-for="(name, index) in movie.actors" :key="index">{{ getActorname(name) }} </div> -->
      <!-- <div v-for="(name, index) in movie.directors" :key="index"> -->
      <!-- <p>{{ name }}</p> -->
      <!-- </div> -->
      <hr />
      <p>{{ movie?.overview }}</p>
    
    </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import img from '@/assets/actorimg.png'
import directorimg from '@/assets/directorimg.png'
import posterimg from '@/assets/noposterimg.png'

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
      // hasuser: true
    };
  },
  created() {
    this.getActorList();
    this.getDirectorList();
  },
  computed: {
    isheart() {
      return this.$store.getters.isheart
    },
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
        // e.target.src = directorimg
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
            
            this.$store.state.heart = !this.$store.state.heart
            console.log(this.$store.state.heart)
          })
          .catch(err => console.log(err))
      }
  },
}

</script>

<style>
.body {
  padding-top: 60px;
}
</style>