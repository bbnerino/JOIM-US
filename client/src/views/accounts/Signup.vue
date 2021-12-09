<template>
  <div >
    <div style="height:30vh"></div>
    <div >
    <h1 >Signup</h1>
    <br>
    <div>
      <label for="username">사용자 이름 &nbsp;&nbsp;</label>
      <input 
        type="text" 
        id="username"
        v-model="credentials.username"
      >
    </div>
      <br>
    <div>
      <label for="password">비밀번호&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;</label>
      <input 
        type="password" 
        id="password"
        v-model="credentials.password"
      >
    </div>
      <br>
    <div>
      <label for="passwordConfirmation">비밀번호 확인 </label>
      <input 
        type="password" 
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
        @keyup.enter="signup"
      >
    </div>
    <br>
    <button @click="signup" class='btn'>회원가입</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          // console.log(res)
          this.$router.push({ name: 'Login'})
        })
        .catch(err => {
          alert('다시 확인해주세요')
          console.log(err)
        })
    }
  }
}
</script>
<style scoped>
  input{ border: 1px solid white; background-color: #e2e2e2; border-radius: value;}
</style>
