<template>
  <div>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="2" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CommentCreate',
  data() {
    return {
      content: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/articles/${this.$route.params.id}/comments/`,
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          location.reload();
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style>
</style>