import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import IntroPage from '@/views/IntroPage.vue'
import NotFound404 from '@/components/NotFound404'
import ArticleView from '@/views/Community/ArticleView'
import LoginView from '@/views/Account/LoginView'
import SignUpView from '@/views/Account/SignUpView'
import CreateView from '@/views/Community/CreateView'
import DetailView from '@/views/Community/DetailView'
import UpdateView from '@/views/Community/UpdateView'
import MyPageView from '@/views/Account/MyPageView'
import MovieDetailView from '@/views/movies/MovieDetailView'
import MovieSearchView from '@/views/movies/MovieSearchView'

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
    path: '/movies/search',
    name: 'MovieSearch',
    component: MovieSearchView
  },
  {
    path: '/movies/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
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
    path:'/mypage/:id',
    name:'MyPageView',
    component: MyPageView,
  },
  {
    path: '/community/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: '/community/create',
    name: 'CreateView',
    component: CreateView
  },
  {
    path: '/community/create/:id',
    name: 'UpdateView',
    component: UpdateView
  },
  {
    path: '/errors/404NotFound',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/errors/404NotFound'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.afterEach(() => {
  window.scrollTo(0,0);
})

export default router
