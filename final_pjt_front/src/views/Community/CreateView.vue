<template>
  <div class="page">
    <div class="container bgcontain54" style="color: #37383A">
      <h1>게시글 작성</h1>
      <div class="mx-auto">
        <form class="size" @submit.prevent="createArticle" @keyup.enter="createArticle">
          <label for="title">제목</label>
          <input class="form-control mt-3 inputtag" placeholder="제목을 입력해주세요" type="text" id="title" v-model.trim="title"><br>
          <label for="content">내용</label>
          <textarea class="form-control mt-3" placeholder="내용을 입력해주세요" id="content" cols="30" rows="15" v-model="content"></textarea><br>
          <button class="custom-btn btn-1 size2" style="color: #37383A">제출</button>
          <router-link :to="{ name: 'ArticleView' }"><button class="custom-btn btn-1 size2" style="color: #37383A">뒤로가기</button></router-link>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
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
        method: 'post',
        url: `${API_URL}/community/articles/`,
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
          this.$router.push({name: 'ArticleView'})
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style>
.size {
  width: 40%;
  margin: auto;
  font-size: 25px;
}
.size2 {
  font-size: 20px;
}

.bgcontain54 {
  margin-top: 5rem;
  background-color: #F2EFE8 ;
  background: linear-gradient(280deg, #F2EFE8 73%, rgba(0,0,0,0) 25%), url(@/assets/scent.jpg);
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