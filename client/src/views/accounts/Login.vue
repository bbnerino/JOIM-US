<template>
  <div>
    <div style="height:30vh">

    </div>
    <div>
      <h1>Login</h1>
      <br>
      <div>
        <label for="username" style="">사용자 이름&ensp;&ensp; </label>
        <input 
          type="text" 
          id="username"
          v-model="credentials.username"
        >
      </div>
      <br>
      <div>
        <label for="password">비밀번호&ensp;&ensp;&ensp;&ensp;&ensp;</label>
        <input @keyup.enter ="login"
          type="password" 
          id="password"
          v-model="credentials.password"
        >
      </div>
      <br>
      <button @click="login">로그인</button>
      <br><br>
      <router-link style="text-decoration:none;  color:white" :to="{ name: 'Signup' }">Signup</router-link> 
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
      is_cannes: false,
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('Itisme',this.credentials.username)
          localStorage.setItem('jwt', res.data.token)
          this.$router.push({name:'LogBrg'})
        })
        .catch((err) => {
          console.log(err)
        })
    },
}}
</script>
<style scoped>
    input{ border: 1px solid white; background-color: #e2e2e2; border-radius: value;}
    label{ font-weight:500;}
</style>