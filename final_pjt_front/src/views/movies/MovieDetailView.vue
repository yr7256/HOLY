<template>
  <div class="body">
    <h1>{{ movie?.title }}</h1>
    <!-- <img :src="MoviePosterurl + `${movie.poster_path}`" alt="" /> -->
    <p>{{ movie?.release_date }}</p>
    <hr />
    <!-- <div v-for="(name, index) in movie.actors" :key="index" > -->
    <!-- <div v-if="actors.id = movie.actors">
      <p v-for="(name, index) in movie.actors" :key="index">{{ name }}</p>
    </div> -->
    <!-- <p> {{ sameId }} </p> -->
    <!-- </div> -->

    <div v-if="actorsLength == actors.length">
      <div v-for="(name, index) in actors" :key="index">{{ name }}</div>
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

export default {
  name: "MovieDetailView",
  data() {
    return {
      movie: null,

      MoviePosterurl: "https://www.themoviedb.org/t/p/w300_and_h450_bestv2",
      actors: [],
      actorsLength: 0,
    };
  },
  created() {
    this.getMovieDetail();
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
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
                this.actors.push(response.data.name);
              })
              .catch((err) => console.log(err));
          }
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style>
.body {
  padding-top: 75px;
  /* 생략 */
}


</style>