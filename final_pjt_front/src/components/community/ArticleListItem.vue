<template>
  <div >
    <!-- <h5>{{ article.id }}</h5> -->
    <div >
      <router-link  
        :to="{ name: 'DetailView', params: { id: article.id} }"
        style="color: #37383A">
        {{ article.title }} | 작성자 : {{ article.username }}
      </router-link>
      <br>
      <hr>
    </div>
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

</style>