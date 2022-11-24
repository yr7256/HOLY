<template>
  <div class="page">
    <div class="container bgcontain">
      <div></div>
      <div class="filmstrip div2">
      </div>
      <br>
      
        <h1 style="color: #37383A" class="h1place">{{ article?.id }}번째 게시글({{ comment_count }})</h1>
        <br>
        <!-- <p class="ptag1" style="color: #37383A">글 번호 : </p> -->
        <p class="ptag1" style="color: #37383A">제목 : {{ article?.title }}</p>
        <p class="ptag1" style="color: #37383A">내용 : {{ article?.content }}</p>
        <p class="ptag1" style="color: #37383A" >작성시간 : {{ article?.created_at }}</p>
        <p class="ptag1" style="color: #37383A">수정시간 : {{ article?.updated_at }}</p>
        <router-link :to="{ name: 'ArticleView' }"><button class="custom-btn btn-1" style="color: #37383A">뒤로가기</button></router-link>
        <router-link :to="{ name: 'UpdateView' }"><button class="custom-btn btn-1" style="color: #37383A">글 수정</button></router-link>
        <button v-show="isAuth" class="custom-btn btn-1" @click="deleteArticle" style="color: #37383A">삭제</button>
          <hr class="my-hr">
          <br>
          <p class="ptag1" style="color: #37383A">댓글 수 : {{ comment_count }}</p>
          <div v-for="(comment, index) in comment_set" :key='index'>
            <p class="ptag1" style="color: #37383A">작성자: {{ comment.comment_user.username }}</p>
            <p class="ptag1" style="color: #37383A"> 댓글 내용: {{ comment.content }}</p>
            <br>
            <button @click="deleteComment(comment.id)" class="custom-btn btn-1" style="color: #37383A">삭제</button><br>
            <!-- <hr class="my-hr"> -->
          </div>
        <hr class="my-hr">
        <br>
        <CommentCreate/>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentCreate from '@/components/community/CommentCreate'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      comment_set: null,
      comment_count: null,
      id: null,
      like_users: []
    }
  },
  created() {
    this.getArticleDetail()
  },
  components: {
    CommentCreate
  },
  computed: {
    isAuth() {
      return this.$store.state.username === this.article.username
    }
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/articles/${this.$route.params.id}/`,
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
        this.comment_set = res.data.comment_set
        this.comment_count = res.data.comment_count
      })
      .catch(err => console.log(err))
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/articles/${this.$route.params.id}/`,
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name: 'ArticleView'})
      })
      .catch(err => console.log(err))
    },
    deleteComment(comment_id) {
      axios({
        method: 'delete',
        url: `${API_URL}/community/comments/${comment_id}/`,
      })
      .then((res) => {
        console.log(res)
        location.reload();
        })
        .catch(err => console.log(err))
    },
    // ArticleLike() {
    //   const like_users = this.like_users
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/communtiy/articles/${this.$route.params.id}/likes/`,
    //     headers: {
    //       Authorization: `Token ${ this.$store.state.token }`
    //     },
    //     data: {
    //       like_users : like_users
    //     }
    //   }),
    //     .then((res) => {
    //       const isLiked =res.data.is_liked
    //       const LikeBtn = 
    //       if (isLiked === true) {

    //       }
    //       console.log(res)
    //       location.reload();
    //     })
    //     .catch(err => console.log(err))

    // }
    // updateComment() {
    //   this.$router.push({
    //     path:"DetailView",
    //     params: {
    //       contentId: this.index
    //       }
    //     })
    //  },

    }
}

</script>

<style>
.bgcontain {
  margin-top: 5rem;
  background-image: #F2EFE8 ;
  /* background: linear-gradient(90deg, #F2EFE8 90%, rgba(0,0,0,0) 25%), url(@/assets/theater.jpg); */
  /* background: 
  linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 59%, rgba(0, 0, 0, 0.65) 100%),
  url(@/assets/movie.png)no-repeat; */
  padding: 0px 0px 60px 0px !important;
  /* border: solid 5px; */
  box-shadow: 0 6px 6px 0px #37383A;
  /* margin-bottom: 10rem; */
  border-radius: 0px 0px  0px;

}
.h1place {
  text-align: left;
  font-weight: bold;
  margin-bottom: 1.5rem;
}
.ptag1 {
  text-align: left !important;
}
.ptag2 {
  text-align: right !important;
}
.custom-btn {
  width: 130px;
  height: 40px;
  padding: 10px 25px;
  border: 2px solid #000;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
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
.filmstrip {
  --background: #151515;
  --size: 15px;
  background-image:
    linear-gradient(to right, var(--background) var(--size), transparent var(--size)),
    linear-gradient(to bottom, var(--background) var(--size), transparent var(--size)),
    linear-gradient(to right, var(--background) var(--size), transparent var(--size)),
    linear-gradient(to bottom, var(--background) var(--size), transparent var(--size)),
    linear-gradient(to bottom, transparent var(--size), var(--background) var(--size));
  background-size: calc(var(--size) * 2) var(--size), calc(var(--size) * 1) var(--size), calc(var(--size) * 2) var(--size), calc(var(--size) * 2) var(--size), 100% calc(100% - var(--size) * 3);
  background-repeat: repeat-x;
  background-position: 0 var(--size), top left, 0 calc(100% - var(--size)), bottom left, 0 var(--size);
  padding: calc(var(--size) * 3) calc(var(--size) * 0.5);
  box-sizing: border-box;
}
.div2 {
  height: 10vh;
  width: 100%;
  color: #F2EFE8;
}
</style>