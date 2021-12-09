<template>
  <div class="sticky-top" style="padding:0 0 0;">
    <v-app-bar color="deep-purple" dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      
      <h1 @click="goMainPage" class="ml-3 mt-2" style="font-size:180%; font-family: 'Caveat', cursive; cursor:pointer" 
      v-if="$route.path != '/movies/recommendedmovies'">&nbsp;JOIM-US </h1>
      <h2 v-else>&nbsp;<img src="https://t1.daumcdn.net/cfile/blog/99066F3A5E40CF6B2D" alt="" width="100px" height="70px"></h2>
      <!-- <v-toolbar-title style="font-weight: 150;">JOIM-US</v-toolbar-title> -->
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary style='height:100vh'>
      <v-list nav>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
        <!-- 아이콘 -->
        <v-list-item-avatar>
          <v-img  src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif"></v-img>
        </v-list-item-avatar>

        <!-- 메인페이지 가기 -->
        <v-list-item >
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
            <router-link :to="{ name: 'MainPage' }" style="text-decoration:none; font-weight:bold; color:black">
              &ensp;  영화목록</router-link>          
        </v-list-item>
        
        <!-- 추천페이지 가기 -->
        <v-list-item >
          <v-list-item-icon>
            <v-icon>fas fa-trophy</v-icon>
            <!-- <i class="fas fa-trophy"></i>           -->
          </v-list-item-icon>
            <router-link :to="{ name: 'LogBrg' }" style="text-decoration:none; font-weight:bold; color:black">
              &ensp;  추천영화</router-link>          
        </v-list-item>
    

        <!-- 리뷰 -->
        <v-list-item >
          <v-list-item-icon>
            <v-icon>fas fa-comments</v-icon>
          </v-list-item-icon>
          <router-link :to="{ name: 'ReviewIndex' }" style="text-decoration:none; font-weight:bold; color:black">&ensp; 리뷰</router-link>
        </v-list-item>

        <!-- 내 프로필 가기 -->
          <v-list-item> 
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <router-link :to="{ name: 'MyProfile' }" style="text-decoration:none; font-weight:bold; color:black"> 
              &ensp;  내 프로필
            </router-link>
          </v-list-item>
          
          
          <!-- 검색창 -->
          <v-list-item> 
            <v-list-item-icon>  
              <v-icon >fas fa-search</v-icon>
            </v-list-item-icon>
              <input type="text" v-model="personName" 
              @keyup.enter="goProfile(personName)"
              placeholder="  유저 검색" style="font-weight:bold; background-color:white">
          </v-list-item>
        <!-- 로그아웃 -->
        <v-list-item >
          <v-list-item-icon>
            <v-icon>fas fa-sign-out-alt</v-icon>
          </v-list-item-icon>
          <v-btn @click="logout" style=" font-weight:bold; ">&ensp;로그아웃</v-btn>
        </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
  export default {
    name:'NavBar',
    data: function() {
      return{
      drawer: false,
      group: null,
      Itisme: null,
      personName: null,
     }
    },
    methods:{
      logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.clear()
      this.Itisme = null
      this.personName = null
      this.$router.push({ name: 'Login' })
    },
      goProfile: function (personName) {
      // console.log(personName)
      this.$router.push({ name: 'Brg', params: { personName, me: localStorage.getItem('Itisme') } })
      this.personName = null
     },
     goMainPage: function(){
      this.$router.push({name:'LogBrg'})
    },
    },
    created: function(){
      this.Itisme = localStorage.getItem('Itisme')
    },
    
  }
</script>

<style>

template{
  font-weight:600;
  color: #90a7d1;
}
</style>