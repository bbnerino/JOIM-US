<template>
  <div>
    <div v-if="existUser">
      <h1 class="my-2" style="color:white; font-size:500%; font-family: 'IM Fell French Canon SC', serif;">Profile</h1>
      <div id='Profile'>
        <br>
      <h2 style="font-weight:700">{{ personName }}님의 페이지입니다.</h2>
      <div class="follow">
        <button @click="follow" v-if="followed" style="font-size:50px;color:blue"><i class="fas fa-handshake"></i></button>
        <button @click="follow" v-if="!followed" style="font-size:50px;opacity:0.3" ><i class="fas fa-handshake"></i></button>
      </div>
      <h5>팔로잉 : {{ followings_count }}명&ensp;&ensp;&ensp;</h5>
      <button >
        <h5 style="cursor:pointer" @click="handle_toggle">팔로워 : {{ followers_count }}명 
          <span v-show="!is_show">▼</span>
          <span v-show="is_show">▲</span>
        </h5>
      </button>
        
      <div v-show="is_show" >
        <div v-for="follower in followers" :key="follower.id">
          <p style="font-weight:700">{{ follower.fields.username }}</p>
        </div>
      </div><br>
        <br>
      <button>
        <h1 style="cursor:pointer; font-weight:700" @click="handle_toggle_two">{{personName}}님이 쓴 리뷰 목록
          <span v-show="!is_show_two">▼</span>
          <span v-show="is_show_two">▲</span>
        </h1>
      </button>
      <div v-show="is_show_two">
        <div v-for="(my_review,index) in my_reviews" :key="my_review.id">
          <h5 style="font-weight:700">{{ index+1 }}. {{ my_review.title }}</h5>
        </div>
      </div>
      </div>
    </div>

    <div class='nop' v-else>
      <h1>떠났나본데요?</h1>
    </div>
    <br>
    <button class="btn btn-info" @click="goHome">내방으로</button>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Profile',
  data: function () {
    return {
      is_show:false,
      is_show_two:false,
      Itisme: null,
      followed: false,
      followers: Object,
      followings: Object,
      followers_count: 0,
      followings_count: 0,
      my_reviews: [],
      existUser: false,
    }
  },
  props: {
    personName: {
      type: String
    },
    me: {
      type: String
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    handle_toggle: function(){
      this.is_show = !this.is_show;
    },
    handle_toggle_two: function(){
      this.is_show_two = !this.is_show_two;
    },
    follow: function () {
      // const review_id = localStorage.getItem('review_id')
      // console.log(this.personName)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/${this.personName}/follow/`,
        headers: this.setToken(),
        data: {
          me: this.Itisme,
          ez_real: true,
        },
      })
        .then(res => {
          // console.log(res)
          this.followed = res.data.followed
          this.followers = JSON.parse(res.data.followers)
          this.followers_count = res.data.followers_count
          this.followings_count = res.data.followings_count
        })
        .catch(err => {
          console.log(err)
        })
    },
    getfollow: function(){
      // console.log(this.personName)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/${this.personName}/follow/`,
        headers: this.setToken(),
        data: {
          me: this.Itisme,
          ez_real: false,
        },
      })
        .then(res => {
          // console.log(res)
          this.followed = res.data.followed
          this.followers = JSON.parse(res.data.followers)
          this.followers_count = res.data.followers_count
          this.followings_count = res.data.followings_count
        })
        .catch(err => {
          console.log(err)
        })
    },
    getReview: function(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.personName}/get_reviews/`,
        headers: this.setToken(),
      })
      .then(res => {
          this.existUser = true
          // console.log(res)
          this.my_reviews = res.data
          // console.log('확인용')
          this.getfollow()
        })
        .catch( {
        })
    },
    goHome: function () {
      this.$router.push({name:'MyProfile'})
    }
  },
  created: function () {
    this.Itisme = localStorage.getItem('Itisme')
    this.getReview({name: 'MyProfile'})
  }
}
</script>

<style scoped>
  .follow >button{
      border: none;
      outline:none;
    }
  h5{
    font-weight: 600;
  }
  .nop >h1{
    margin-top: 300px;
    font-size: 500%;
  }
  #Profile{
    height: 100vh;
    font-weight:700;
    background-color:#ece6cc ;
    color: black;
  }
</style>