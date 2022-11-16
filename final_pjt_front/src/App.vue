<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'MovieView' }">Main</router-link> |
      <router-link :to="{ name: 'ArticleView' }">Community</router-link> |
      <router-link :to="{ name: 'LoginView' }">Login</router-link> |
      <router-link :to="{ name: 'MovieDetailView' }">Movie Detail</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #2c3e50;
}
</style>
