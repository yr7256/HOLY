<template>
  <div>
    <h3 class= "cc" style="color: #37383A">댓글쓰기</h3>
    <form class="comment" @submit.prevent="createComment" @keyup.enter="createComment">
      <label style="color: #37383A" class="form-label cc2" for="content">내용 입력</label>
      <input class="form-control inputtag" id="content"  v-model="content"><br>
      <button class="custom-btn btn-1" type="submit" id="submit" style="color: #37383A">제출</button>
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
.comment {
  width: 400px;
  /* margin-left: 20.5rem; */
  text-align: center;
  justify-content: center;
  /* margin-left: 28rem; */
}
.bgcontain3 {
  /* margin-top: 1rem; */
  /* background-image: #F2EFE8 ; */
  background-color:  #F2EFE8 !important;
  padding: 30px;
  /* border: solid 5px; */
  /* box-shadow: 0 3px 4px 0px grey; */
  /* margin-bottom: 10rem; */
  /* border-radius: 0px 0px  0px; */
  margin-bottom: 3rem;

}
.cc {
  margin-right: 72.5rem;
}
.cc2{
  text-align: left;
  margin-right: 8rem;
}
</style>