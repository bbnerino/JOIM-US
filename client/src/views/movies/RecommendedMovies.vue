<template>
  <div><br>
    <h1 style="color:white; font-size:700%; font-family: 'IM Fell French Canon SC', serif;">Palme D'or</h1>

    <div v-if="is_null" id="noActor">
      <h1>이런! 아직 찜한 배우가 없으시군요!</h1>
      <br>
      <button class="btn btn-warning" >
        <router-link ink :to="{ name: 'PreferenceCheck' }" style="text-decoration:none; font-weight:bold; color:white">갑시다!</router-link>
      </button>
    </div>

    <div v-else> 
      <movie-splide 
        :recommended_movies_one=recommended_movies_one
        :recommended_movies_two=recommended_movies_two
        :reco_genre_one=reco_genre_one
        :reco_genre_two=reco_genre_two  
      ></movie-splide>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieSplide from '@/views/movies/MovieSplide'
export default {
  name: 'RecommendedMovies',
  components:{ MovieSplide },
  data() {
    return{
      Itisme: null,
      Itisme_id: null,
      is_null: false,
      recommended_movies_one: [],
      // recommended_movies_one: ['','','','','','','','','',''],
      // recommended_movies_two: ['','','','','','','','','',''],
      recommended_movies_two: [],
      reco_genre_one: null,
      reco_genre_two: null,
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
    getRecommendedMovies: function () {
      axios({
        method:`get`,
        url: `http://127.0.0.1:8000/movies/${this.Itisme_id}/getrecommendedmovies/`,
        headers: this.setToken(),
      })
        .then(res=>{
          console.log(res)
          if (res.data[0].one === null && res.data[1].two === null) {
            this.is_null = true
          } else {
          this.recommended_movies_one = res.data[0].one
          this.recommended_movies_two = res.data[1].two
          this.reco_genre_one = res.data[2].one_genre
          this.reco_genre_two = res.data[3].two_genre
          }
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
  created () {
    this.Itisme_id = localStorage.getItem('Itisme_id')
  },
  mounted () {
    this.getRecommendedMovies()
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=IM+Fell+French+Canon+SC&family=Parisienne&display=swap');
#noActor{
  margin-top: 200px;
}
</style>