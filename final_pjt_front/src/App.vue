<template>
  <div id="app">
    <HeaderItem/>
  </div>
</template>
<script>
import HeaderItem from '@/components/HeaderItem.vue'
import "./assets/css/index.scss"

export default ({
  components: {
    HeaderItem,
  },
})
</script>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
  width: 100%;
  min-width: 600px;
}

/* nav {
  padding: 30px;
  width: 100%;
  min-width: 600px;
} */

/* nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
} */

/* nav a.router-link-exact-active {
  color: #2c3e50; */

/* nav a.router-link-exact-active {
  color: white;
>>>>>>> 831014a5935da594472c0fee06d888b91f5994c0
} */
</style>
