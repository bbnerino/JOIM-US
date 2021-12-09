<template>
  <div>
    <img   
    style="width:30vh; margin-top:30vh"
    src="@/img/하얀칸.png" alt="">
  </div>
</template>

<script>
import axios from 'axios';
export default {
name : 'LogBrg',
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
  }
},
    
created: function () {
    this.setmyid()
    setTimeout(function () {
        this.$emit('login')
        this.$router.push({name: 'RecommendedMovies'})
    }.bind(this), 2500); 
  }
}

    



</script>

<style>

</style>