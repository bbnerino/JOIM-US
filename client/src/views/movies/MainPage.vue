<template>
  <div>
    <br>
    <h1 style="color:white; font-size:700%; font-family: 'IM Fell French Canon SC', serif;">Cannes</h1>

    
    <div class="container  justify-content-around" style=" margin-top:20px;"  >
      <div class="offset-7">
        <select  style="width:100px;  border-radius: 5px; " v-model="select_type">
          <!-- <option selected disabled hidden :value="null">&nbsp;검색 ▼</option> -->
          <option value="movie_name">영화 제목</option> 
          <option value="actor_name">배우 이름</option>
        </select>
        &nbsp;
        <input style="border-radius: 5px;" type="text" v-model="find_word" @keyup.enter="find_movies" /> &nbsp;
        <button class="btn btn-info btn-sm" @click="find_movies">검색</button>
      </div>
      <div class="offset-">
        <div v-if="is_searched">
            <h1 style="text-align:left">&ensp; "{{ search_result }}" 에 대한 검색 결과 ({{ search_count }})</h1>
            <button class="btn btn-danger btn-sm" @click="Reset">리셋</button> 
        </div>
        <div v-else >
          <h1 style="text-align:left"> &ensp; 전체 ({{ search_count }})</h1>
        </div>
      </div>  
      <div class="row mx-auto" style=" margin-left:50px;">
        <div class='col-3' v-for="movie in movies"  :key="movie.id" >
         <movie-card :movie=movie> </movie-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/views/movies/MovieCard.vue'
// import Carousel from '@/components/Carousel.vue'
export default {
  name: 'MainPage',
  data: function() {
    return {
      movies: [],
      find_word: null,
      select_type: 'movie_name',
      URL: 'https://image.tmdb.org/t/p/w500/',
      search_result: null,
      is_searched: false,
      search_count: 0,
    }
  },
  components:{
    MovieCard,
    // Carousel
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    setmyid: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/set_my_id/',
        headers: this.setToken(),
        data: {
          me: localStorage.getItem('Itisme')
        }
      })
        .then(res => {
          // console.log(res)
          localStorage.setItem('Itisme_id', res.data.user_id)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.movies = res.data
          this.search_count = res.data.length
        })
        .catch(err => {
          console.log(err)
        })
    },
    detailMovie: function (movie) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          localStorage.setItem('movie_id',res.data.id)
          localStorage.setItem('movie_title', res.data.title)
          localStorage.setItem('movie_overview', res.data.overview)
          localStorage.setItem('movie_poster_path', res.data.poster_path)
          this.$router.push({ name: 'DetailMovie'})
        })
        .catch(err => {
          console.log(err)
        })
    },
    find_movies: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/movies/selectmovies/',
        headers: this.setToken(),
        data: {
          find_word: this.find_word,
          select_type: this.select_type,
        }
      })
        .then(res => {
          console.log(res)
          this.movies = res.data
          this.is_searched = true
          this.search_result = this.find_word
          this.search_count = res.data.length
        })
        .catch(err => {
          console.log(err)
        })
    },
    Reset: function () {
      this.is_searched = false
      this.search_result = this.find_word
      this.select_type = 'movie_name'
      this.find_word = null
      this.getMovies()
    }
  },
  created: function () {
    this.setmyid()
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({name: 'Login'})
    }
  },
  
}
</script>

<style scoped>
  container{
    display: flex;
  }
</style>