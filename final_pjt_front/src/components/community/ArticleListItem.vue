<template>
  <div >
    <!-- <h5>{{ article.id }}</h5> -->
    <router-link
      :to="{ name: 'DetailView', params: { id: article.id} }"
    >
      {{ article.title }} | 작성자 : {{ article.username }}
    </router-link>
    <br>
    <hr>
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

</style>