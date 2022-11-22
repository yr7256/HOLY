<template>
  <div class="body">
    <h1>게시글 작성</h1>
    <div class="mx-auto articleboxcolor">
      <form class="size" @submit.prevent="createArticle" @keyup.enter="createArticle">
        <label for="title">제목</label>
        <input class="form-control mt-3 inputtag" placeholder="제목을 입력해주세요" type="text" id="title" v-model.trim="title"><br>
        <label for="content">내용</label>
        <textarea class="form-control mt-3" placeholder="내용을 입력해주세요" id="content" cols="30" rows="15" v-model="content"></textarea><br>
        <button class="btn-gradient yellow btn-size">제출</button>
        <router-link :to="{ name: 'ArticleView' }"><button class="btn-gradient yellow btn-size">뒤로가기</button></router-link>
      </form>
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
.body {
  padding-top: 60px;
}
.size {
  width: 50%;
  margin: auto;
  font-size: 25px;
}
.articleboxcolor {
  background-color: black;
  width: 1200px;
  height: 750px;
}
</style>