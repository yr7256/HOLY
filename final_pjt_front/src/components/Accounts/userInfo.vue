<template>
  <div>
    <nav class="col-4">
      <h1>User info</h1>
    </nav>
    <nav class="userInfo">
      <div>{{ $store.state.username }}</div>
      <div>게시글:  {{ $store.state.articles.length }} 개 </div>
    </nav>
    <div v-if="$store.state.articles.length > 0">
        <!-- 리뷰 리스트 -->
        <ul class="list-group list-group-flush list-group-numbered mx-5">
          <li 
            class="
              list-group-item
              d-flex
              justify-content-between
              align-items-start
              bg-transparent
              text-white
              border-bottom
              my-1"
            v-for="(review, index) in reviewsPerPage[reviewCurrentPage-1]"
            :key="index"
            @dblclick="onClickReview(review.pk)"
          >
            <div class="ms-2 me-auto">
              <h5 class="fw-bold">
                {{$store.state.articles.title}}
              </h5>
              <div class="text-start">
                {{ $store.state.articles.length > 20 ?  $store.state.articles.title.slice(0, 20) + '...' :  $store.state.articles.title }}
              </div>
            </div>
          </li>
        </ul>
 
    
      </div>
      <div v-else class="fw-bold text-start text-white mx-5">
        <h4>리뷰가 없네요..</h4>
      </div>
    </div>
    
    

</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'userInfo',
  data: function () {
    return {
      // reviewCurrentPage: 1
      
    }  
  },
  // methods: {
  //   // onClickReview(review_id){
  //     this.$router.push({
  //       name: "ArticleView",
  //       // params: { article.username },
  //     });
  //   },
  // },
  // methods: {
  //   getInfo() {
  //     this.username = sessionStorage.getItem('username')
  //     const token = sessionStorage.getItem('jwt')
  //     // const user_id = jwtDecode(token).user_id
  //     const options = {
  //       headers: {
  //         Authorization: `JWT ${token}`
  //       }
  //     }
  //     axios.get(API_URL+'/accounts/', options)
  //   }
  // }, 

    
}

</script>

<style>

</style>