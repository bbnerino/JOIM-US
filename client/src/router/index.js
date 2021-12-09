import Vue from 'vue'
import VueRouter from 'vue-router'
// import TodoList from '@/views/todos/TodoList'
// import CreateTodo from '@/views/todos/CreateTodo'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MainPage from '@/views/movies/MainPage'
import RecommendedMovies from '@/views/movies/RecommendedMovies'
import DetailMovie from '@/views/movies/DetailMovie'
import ReviewIndex from '@/views/community/ReviewIndex'
import CreateReview from '@/views/community/CreateReview'
import DetailReview from '@/views/community/DetailReview'
import MyProfile from '@/views/accounts/MyProfile'
import Profile from '@/views/accounts/Profile'
import PreferenceCheck from '@/views/accounts/PreferenceCheck'
import Brg from '@/views/accounts/Brg'
import MovieSplide from '@/views/movies/MovieSplide'
import LogBrg from '@/views/accounts/LogBrg'
Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/todos',
  //   name: 'TodoList',
  //   component: TodoList,
  // },
  // {
  //   path: '/todos/create',
  //   name: 'CreateTodo',
  //   component: CreateTodo,
  // },
  {
    path: '/accounts/logbrg',
    name: 'LogBrg',
    component: LogBrg,
  },
  {
    path: '',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies/mainpage',
    name: 'MainPage',
    component: MainPage,
  },
  {
    path: '/movies/detailmovie',
    name: 'DetailMovie',
    component: DetailMovie,
  },
  {
    path: '/community/reviewindex',
    name: 'ReviewIndex',
    component: ReviewIndex,
  },
  {
    path: '/community/detailreview',
    name: 'DetailReview',
    component: DetailReview,
  },
  {
    path: '/community/createreview',
    name: 'CreateReview',
    component: CreateReview,
  },
  {
    path: '/accounts/myprofile',
    name: 'MyProfile',
    component: MyProfile,
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile,
    props: true,
  },
  {
    path: '/accounts/brg',
    name: 'Brg',
    component: Brg,
    props: true,
  },
  {
    path: '/movies/moviesplide',
    name: 'MovieSplide',
    component: MovieSplide,
  },
  {
    path: '/movies/recommendedmovies',
    name: 'RecommendedMovies',
    component: RecommendedMovies,
  },
  {
    path: '/accounts/prefrencecheck',
    name: 'PreferenceCheck',
    component: PreferenceCheck,
  },
  
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
