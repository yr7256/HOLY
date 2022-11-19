<template>
  <div class="body">
    <h1>게시글 작성</h1>
    <p>{{ article }}</p>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
    <router-link :to="{ name: 'ArticleView' }"><button>뒤로가기</button></router-link>
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
        this.$router.push({name: 'ArticleView'})
      })
      .catch(err => console.log(err))
    },
  }
}
</script>

<style>
.body {
  padding-top: 75px;
  /* 생략 */
}

</style>