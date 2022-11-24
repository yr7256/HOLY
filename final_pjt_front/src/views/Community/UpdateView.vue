<template>
  <div class="page">
    <div class="container bgcontain62" style="color: #37383A">
      <h1>게시글 작성</h1>
      <div class="mx-auto">
        <form class="size" @keyup.enter="updateArticle" @submit.prevent="updateArticle">
          <label for="title">제목</label>
          <input class="form-control mt-3 inputtag" type="text" id="title" v-model.trim="title"><br>
          <label for="content">내용</label>
          <textarea class="form-control mt-3" id="content" cols="30" rows="15" v-model="content"></textarea><br>
          <button class="custom-btn btn-1 size2" style="color: #37383A">제출</button>
          <router-link :to="{ name: 'DetailView' }"><button class="custom-btn btn-1 size2" style="color: #37383A">뒤로가기</button></router-link>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateView',
  data() {
    return {
      article: null,
      title: null,
      content: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/articles/${this.$route.params.id}/`,
      })
      .then((res) => {
        console.log(res)
        this.title = res.data.title
        this.content = res.data.content
      })
      .catch(err => console.log(err))
    },
    updateArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/community/articles/${this.$route.params.id}/`,
        data: {
          title: title,
          content: content,
        },
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name: 'DetailView'})
      })
      .catch(err => console.log(err))
    },
  }
}
</script>

<style>
.size {
  width: 40%;
  margin: auto;
  font-size: 25px;
}

.bgcontain62 {
  margin-top: 3.5rem;
  background-color: #F2EFE8 ;
  background: linear-gradient(280deg, #F2EFE8 78%, rgba(0,0,0,0) 25%), url(@/assets/famous.PNG);
  /* background: 
  linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0) 59%, rgba(0, 0, 0, 0.65) 100%),
  url(@/assets/movie.png)no-repeat; */
  padding: 30px 60px  !important;
  /* border: solid 5px; */
  box-shadow: 0 6px 6px 0px #37383A;
  /* margin-bottom: 10rem; */
  border-radius: 0px 0px  0px;

}
</style>