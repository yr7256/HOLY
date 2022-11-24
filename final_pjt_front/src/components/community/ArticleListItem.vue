<template>
  <div >
    <!-- <h5>{{ article.id }}</h5> -->
    <!-- <div class=""> -->
      <router-link class="a3"
        :to="{ name: 'DetailView', params: { id: article.id} }"
        style="color: #37383A">
        {{ article.title }} | 작성자 : {{ article.username }}
      </router-link>
      <br>
      <hr>
    <!-- </div> -->
  </div>
</template>

<script>

export default {
  name: 'ArticleListItem',
  props: {
    article: Object
  },
  methods: {
 
}
}
</script>

<style>
.cc {
  text-align: center;
}
.a3 {
  color: #37383A !important;
}

</style>