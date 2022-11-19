<template>
  <div class="body">
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    {{ article }}
    <router-link :to="{ name: 'ArticleView' }"><button class="btn-gradient yellow mini">뒤로가기</button></router-link>
    <router-link :to="{ name: 'UpdateView' }"><button class="btn-gradient yellow mini">글 수정</button></router-link>
    <button class="btn-gradient yellow mini" @click="deleteArticle">삭제</button>
    <div>
      
      <p>댓글 수 : {{ comment_count }}</p>
      <div v-for="(comment, index) in comment_set" :key='index'>
        <p>댓글 내용: {{ comment.content }}</p>
        <!-- <button @click="updateComment" class="btn-gradient yellow mini">수정</button> -->
        <p @click="deleteComment" class="btn-gradient yellow mini">삭제</p><br>
      </div>
  </div>
    <CommentCreate/>
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
      id: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  components: {
    CommentCreate
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
        this.id = res.data.id
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
    deleteComment() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/comments/${this.comment_set.index}/`,
        
      })
      .then((res) => {
        console.log(res)
        // this.comment_set.splice(this.comment_set.index, 1)
        this.$router.push({
          path:"DetailView"}) 
        })
        .catch(err => console.log(err))
      
    },
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
.body {
  padding-top: 75px;
  /* 생략 */
}
</style>