<template>
  <div class="hovertest " @mouseover="show=true" @mouseleave="show=false" >
      <v-card class="mx-auto " max-width="344" style="background-color:rgb(19, 14, 14)">
        <div class="img_box">
          <figure class="ho">
            <v-img :src="`${URL + movie.poster_path}`" height="500px"
            style="cursor:pointer" @click="detailMovie(movie)"></v-img>
          </figure>
        </div>
      <v-card-title>
        <p style="font-weight:bold; color:white;" >{{ movie.title }}</p>
      </v-card-title>

      <v-card-actions class="row">
        <div class="col-12">
          <v-btn class="float-right btn"  text  @click="detailMovie(movie)" >
          <h4 style=" color:white;"> 상세페이지</h4>
        </v-btn>
        </div>
        <v-spacer></v-spacer>
        <!-- <v-btn icon @click="show = !show" style="color:white;">
          <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
        </v-btn> -->
      </v-card-actions>

      <v-expand-transition>
        <div v-show="show">
          <v-divider></v-divider>
          <v-card-text>  
          <p style="font-weight:bold; color:white;">{{overview}}</p>
          </v-card-text>
        </div>
       </v-expand-transition>
      </v-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'MovieCard',
  props:{movie:Object},
  data: function() {
    return {
      URL: 'https://image.tmdb.org/t/p/w500/',
      show: false,
      overview: this.movie.overview.substring(0,98)+"..."
    }
  },
  
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
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
    }
  },
}
</script>

<style>
.img_box{
  overflow: hidden;
}
.hovertest:hover .ho {
  transform: scale(1.08);
  transition: 0.8s;
}
  text{
    font-weight: 200;
  }
  .rounded-card{
    border-radius:50px;
}
.hovertest:hover{
  transform: scale(1.05);
  transition: 0.5s;
}

</style>