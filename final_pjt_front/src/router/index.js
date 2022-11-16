import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import IntroPage from '@/views/IntroPage.vue'
import NotFound404 from '@/components/NotFound404'
import ArticleView from '@/views/Community/ArticleView'
import LoginView from '@/views/Account/LoginView'
import SignUpView from '@/views/Account/SignUpView'
import CreateView from '@/views/Community/CreateView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'IntroPage',
    component: IntroPage
  },
  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/community',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/errors/404NotFound',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: 'community/create',
    name: 'CreateView',
    component: CreateView
  },
  {
    path: '*',
    redirect: '/errors/404NotFound'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
