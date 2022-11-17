<template>
  <div>
    <!-- <h5>{{ article.id }}</h5> -->
    <router-link
      :to="{ name: 'DetailView', params: { id: article.id} }"
    >
    <span>
      {{ article.title }} | 작성자 : {{ article.username }}
    </span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object
  },
}
</script>

<style>
a {
  text-decoration: none;
}
</style>