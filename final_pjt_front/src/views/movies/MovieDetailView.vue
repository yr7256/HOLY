<template>
  <div class="body">
    <h1>{{ movie?.title }}</h1>
    <img :src="MoviePosterurl + `${movie.poster_path}`" @error="noPosterImg" />
    <p>{{ movie?.release_date }}</p>
    <hr />
    <!-- <div v-for="(name, index) in movie.actors" :key="index" > -->
    <!-- <div v-if="actors.id = movie.actors">
      <p v-for="(name, index) in movie.actors" :key="index">{{ name }}</p>
    </div> -->
    <!-- <p> {{ sameId }} </p> -->
    <!-- </div> -->
    
    <!-- <div v-if="actorsLength == actors.length"> -->

    <!-- <div class="row row-cols-auto row-cols-md-3 g-2"> -->
      <div class="col" v-for="(name, index) in directors" :key="index">
        <div class="card h-80 w-80">
          <a :href="personDetailurl + `${name.id}`">
            <img class="card-img-top" style="width:100px; height:100px;" :src="MoviePosterurl+`${name.profile_path}`" alt="" @error="noDirectorImg">
          </a>
          <div class="card-body">
            <p class="card-title">{{ name.name }}</p>
          </div>
        </div>
      </div>
    <!-- </div> -->
    <br>
    <div class="row row-cols-auto row-cols-md-3 g-2">
      <div class="col" v-for="(name, index) in actors" :key="index">
        <div class="card h-80 w-80">
          <a :href="personDetailurl + `${name.id}`">
            <img class="card-img-top" style="width:100px; height:100px;" :src="MoviePosterurl+`${name.profile_path}`" alt="" @error="noImage">
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
      directors: []
    };
  },
  created() {
    this.getActorList();
    this. getDirectorList();
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
      }

  },
}
</script>

<style>
.body {
  padding-top: 75px;
  /* 생략 */

}


</style>