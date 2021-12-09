<template>
  <div>
    <br>
    <h1 style="color:white; font-size:700%; font-family: 'IM Fell French Canon SC', serif;">Croisette</h1>


    <hr>
    <ul class="list-group" style="background-color:#ece6cc"
    v-for="(review,i) in reviews" :key="i"  >
      <br>
      
      <li class="list-group-item" 
      style="text-align:left; color:black; background-color:#f5f5dc">
        <h2 @click="detailReview(review)" style="cursor:pointer; display:inline-block">{{i+1}}.{{ review.title }}</h2>
        <p style="font-size:90%"> {{ review.movie }}</p>
      </li>
      <br>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name : 'ReviewIndex',
  components:{
  },
  data: function() {
    return {
      reviews: [],
      movies: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    matching: function () {
       this.reviews.forEach(review_each => {
        this.movies.forEach(movie_each => {
          if (review_each.movie === movie_each.id) {
            review_each.movie = movie_each.title
          }
        })
      })
    },
    getReviews: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.reviews = res.data
          this.getMovies()
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
          this.matching()
        })
        .catch(err => {
          console.log(err)
        })
    },
    detailReview: function (review) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${review.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          localStorage.setItem('review_id', res.data.id)
          localStorage.setItem('movie_name', review.movie)
          this.$router.push({ name: 'DetailReview'})
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getReviews()
    } else {
      this.$router.push({name: 'Login'})
    }
  },
}
</script>

<style>
  
  @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=IM+Fell+French+Canon+SC&display=swap');

</style>