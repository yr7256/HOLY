import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import GAuth from 'vue-google-oauth2'

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

const gauthOption = {
  clientId: '1025901526115-cvgcig9fl391aj9ruhoues7onofeghrj.apps.googleusercontent.com.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}
Vue.use(GAuth, gauthOption)