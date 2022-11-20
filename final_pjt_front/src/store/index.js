import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'
// const FRONT_URL = 'http://localhost:8080'



export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    articles: [],
    token: null,
    username: null
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token){
      state.token = token.key
      state.username = token.username
      router.push({name: 'MovieView'})
    },
    LOGOUT (state) {
      state.username = null
      state.token = null
      localStorage.removeItem('username')
      localStorage.removeItem('token')
      location.reload();
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_USERID(state, userid) {
      state.userid = userid
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/community/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch(err => console.log(err))
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
    axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', {'key': res.data.key, 'username': username})
        })
        .catch(err => console.log(err))
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', {'key': res.data.key, 'username': username})
        })
        .catch(err => console.log(err))
    },
    logout(context) {
      context.commit('LOGOUT')
    },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
          console.log(res.data)
        })
        .catch(err => console.log(err))
    },
    getUserid(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('GET_USERID', res.data.pk)
          // this.userid = res.data.pk
          // location.reload();
        })
        .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
