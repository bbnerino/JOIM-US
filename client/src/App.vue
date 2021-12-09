<template>   
  <body>
    <div id="app">
    <span v-show="isLogin">
      <nav-bar id="nav" class="nav"></nav-bar>
    </span>
    <!-- <span v-else style="float:right" >
      <router-link :to="{ name: 'Signup' }">Signup</router-link> |
      <router-link :to="{ name: 'Login' }">Login</router-link> 
    </span> -->
    
      
      <router-view @login="isLogin=true"/>
    </div>
  </body>
</template>

<script>
import NavBar from '@/views/community/NavBar.vue';
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      // personName: null,
      // Itisme: localStorage.getItem('Itisme'),
    }
  },
  components:{
    NavBar,
  },
  
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.clear()
      this.personName = null
      this.$router.push({ name: 'Login' })
    },
    goProfile: function (personName) {
      // console.log(personName)
      this.$router.push({ name: 'Brg', params: { personName, me: localStorage.getItem('Itisme') } })
      this.personName = null
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      // const token = localStorage.getItem('jwt')
      this.Itisme = localStorage.getItem('Itisme')
      this.isLogin = true
    }
    // if (token) {
    // }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding:wght@700&display=swap');
html { height: 100%; }
body{ 
  height: 100%;
  background: linear-gradient(rgb(17, 17, 17),rgb(28, 28, 31),   rgb(31, 31, 32),rgb(25, 25, 27),rgb(17, 17, 17));
  /* background: linear-gradient(rgb(160, 32, 160),rgb(21, 23, 138),
  rgb(45, 180, 180),rgb(74, 156, 92),rgb(160, 32, 160)); */
}


#app { 
  font-family: 'Nanum Gothic Coding', monospace;
  /* font-family: 굴림, Helvetica, Arial, sans-serif; */
  text-align: center;
  color: #edeff1; 
  /* 텍스트 색깔 */
}

#nav {
  padding: 30px;
}


#nav a {
  font-weight: bold;
  color: #788694;
}

#nav a.router-link-exact-active {
  color: #1a5339;
}
#nav a.router-link-exact-active {
  color: #185238;
}
.fixed-tabs-bar .v-tabs__bar {
    position: -webkit-sticky;
    position: sticky;
    top: 4rem;
    z-index: 2;
}
</style>
