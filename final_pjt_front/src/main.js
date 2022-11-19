import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

import Meta from 'vue-meta'
Vue.use(Meta, {
  attribute: 'data-vue-meta'
})
