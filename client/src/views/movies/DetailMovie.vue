<template>
<div>

    <p style="font-size: 66px; margin:40px">{{ movie.title }}</p>
      
    <div class="container">
    <div class="row d-flex " >
      <!-- <div class="col-6" style="display:inline-block"> -->
        <img class="col-4 offset-2" :src="`${URL + movie.poster_path}`"  
        style="border-radius: 3%;">
      <!-- </div> -->

      <div class="col-4 " >
        <p class='text-align:center'>{{ movie.overview }}</p>
      </div>

      <br><br>
    </div>
    </div>
    
    <h1 class="m-5"><router-link :to="{ name: 'CreateReview', params: {update_review: { title: null }, for_update: false} }" 
        style="text-decoration:none; color:white">리뷰작성</router-link></h1>
    <br><br><br>
    <!-- 출연 배우 목록 -->
    <div class="container">
      <div class="row">
        <div class="col-2" v-for="actor in actors" :key="actor.id">
          <img style="margin-top:20px;" :src="`${URL + actor.profile_path}`" alt="profile_path" width=50%>
          <h2>{{ actor.name }} <input type="checkbox" :value="`${actor.actor_id}`" :id="`${actor.actor_id}`" v-model="checked_actors" @change="changedLike(actor.actor_id)"></h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DetailMovie',
  data: function () {
    return {
      URL: 'https://image.tmdb.org/t/p/w500/',
      ex4: 'warning',
      movie: {
        id: null,
        title: null,
        overview: null,
        poster_path: null,
      },
      actors: [],
      checked_actors: [],
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
    getDetailMovie: function () {
      this.movie.id = localStorage.getItem('movie_id')
      this.movie.title = localStorage.getItem('movie_title')
      this.movie.overview = localStorage.getItem('movie_overview')
      this.movie.poster_path = localStorage.getItem('movie_poster_path')
      this.getActorMovie()
      this.getMyActors()
    },
    getActorMovie: function () {
      axios({
        method:`get`,
        url: `http://127.0.0.1:8000/movies/get_actors/${this.movie.id}/`,
        headers: this.setToken(),
      })
        .then(res=>{
          console.log(res)
          this.actors = res.data
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getMyActors: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${localStorage.getItem('Itisme_id')}/getmyactors/`,
        headers: this.setToken(),
      })
      .then(res => {
          console.log(res)
          res.data.my_actor_list.forEach(element => {
            if (!this.checked_actors.includes(String(element.actor_id))) {
              this.checked_actors.push(String(element.actor_id))
            }
          })
          // console.log(this.checked_actors)
        })
        .catch(err => {
          console.log(err)
        })
    },
    changedLike: function(my_actor_id) {
      // console.log(my_actor_id)
      // console.log(this.checked_actors)
      if (this.checked_actors.includes(String(my_actor_id))){
        this.is_is_put = true
      } else {
        this.is_is_put = false
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/${localStorage.getItem('Itisme_id')}/likethisactor/${my_actor_id}/`,
        headers: this.setToken(),
        data: {
          is_put: this.is_is_put
        }
      })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getDetailMovie()
  },
}
</script>

<style>
  p{
    font-size: 18px;
    font-weight: 600;
  }
</style>