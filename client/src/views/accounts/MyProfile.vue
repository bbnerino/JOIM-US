<template>
  <div>
  <div id="MyProfile" >
    <br>
    <h1 style="font-weight:600; font-size:80px; font-family: 'IM Fell French Canon SC', serif;">My Room</h1><br>
    <h2 style="font-weight:600">{{ Itisme }}님 반갑습니다.</h2><br>
    <p>당신의 페이지를 직접 꾸며보세요!</p>
    <br>
    <input type="text" @keyup.enter="just_for_fun(false)" v-model="calar" placeholder="brown"><button @click="just_for_fun(false)" class="btn btn-sm btn-primary">폰트 색상 변경</button>
    <br><br>
    <input type="text" v-model="bg_calar[0]" placeholder="ivory">
    <input type="text" v-model="bg_calar[1]" placeholder="skyblue">
    <input @keyup.enter="just_for_fun(true)" type="text" v-model="bg_calar[2]" placeholder="hotpink">
    <button @click="just_for_fun(true)" class="btn btn-sm btn-primary">배경 색상 변경</button>
    
    <hr>
    <!-- 모달창  -->
    <p >팔로잉 : {{ followings_count }}&ensp;&ensp;&ensp;</p>

    <p style="cursor:pointer" @click="handle_toggle">팔로워 : {{ followers_count }} 
      <span v-show="!is_show">▼</span>
      <span v-show="is_show">▲</span></p>
    <div v-show="is_show" >
      
      <div v-for="follower in followers" :key="follower.id">
        <h6>{{ follower.fields.username }}</h6>
      </div>
    </div> <br>
      



    <button style="cursor:pointer; " @click="handle_toggle_two"><h1>내가 쓴 리뷰
      <span v-show="!is_show_two">▼</span>
      <span v-show="is_show_two">▲</span></h1>
    </button>

    <div v-show="is_show_two" ><br>
      <div v-for="(my_review,index) in my_reviews" :key="my_review.id">
        <h5 style="cursor:pointer; font-weight:600 " @click="goMyDetailReview(my_review.id)">{{index+1}}. {{ my_review.title }}</h5>
        <br>
      </div>
      <!-- <v-btn @click="handle_toggle_two" type="button"
        elevation="1" x-small>닫기</v-btn>-->
    </div> <br> 
    <br>
    <br>
    <br>

    
    <button  @click="getMyActors"><h1>내가 좋아하는 배우들
      <span v-show="!is_show_actor">▼</span>
      <span v-show="is_show_actor">▲</span></h1></button>
    <br>
    <div  v-show="is_show_actor" ><br>
      <!-- <v-btn @click="getMyActors" type="button" elevation="1" small>닫기</v-btn> -->
      <div v-for="my_actor in my_actors" :key="my_actor.id">
        <h5 style="font-weight:600">{{ my_actor.name }} &nbsp; 
          <input style="width: 18px;
            height: 18px;" type="checkbox"  id="chk" :value="`${ my_actor.actor_id }`" v-model="checked_actors" @change="changedLike(my_actor.actor_id)">
          <!-- <v-checkbox color="success" :on-icon="'mdi-heart'" :off-icon="'mdi-heart-outline'" :id="`${ my_actor.actor_id }`" :value="`${ my_actor.actor_id }`" v-model="checked_actors" @change="changedLike(my_actor.actor_id)"></v-checkbox> -->
        </h5>
      </div>
      
    </div>
    <br><br><br>
    <router-link :to="{ name: 'PreferenceCheck' }" style="text-decoration:none; font-weight:bold; color:black; font-size:30px">
    <i class="fas fa-plus"></i></router-link>
  </div>
</div>
</template>

<script>
import axios from 'axios'

// function just_for_fun (font_color, bg_color) {
//   return
// }
// const r = document.querySelector(':root');
// r.style.setProperty('--calar', 'orange');
// const rs = getComputedStyle(r);


export default {
  name: 'Profile',
  data: function () {
    return {
      is_show: false,
      is_show_two: false,
      is_show_actor:false,
      Itisme: null,
      Itisme_id: 0,
      followers: Object,
      followings: Object,
      followers_count: 0,
      followings_count: 0,
      my_reviews: [],
      my_actors: [],
      checked_actors: [],
      is_is_put: null,
      calar: null,
      bg_calar: ['', '', ''],
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
    handle_toggle: function(){
      this.is_show = !this.is_show;
    },
    handle_toggle_two: function(){
      this.is_show_two = !this.is_show_two;
    },
    getfollow: function(){
      // console.log(this.personName)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/${this.Itisme}/follow/`,
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
        url: `http://127.0.0.1:8000/community/${this.Itisme}/get_reviews/`,
        headers: this.setToken(),
      })
      .then(res => {
          // console.log(res)
          this.my_reviews = res.data
          // console.log('확인용')
          this.getfollow()
        })
        .catch(err => {
          console.log(err)
        })
    },
    goMyDetailReview: function (idyo) {
      localStorage.setItem('review_id', idyo)
      this.$router.push({name: 'DetailReview'})
    },
    getMyActors: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.Itisme_id}/getmyactors/`,
        headers: this.setToken(),
      })
      .then(res => {
          this.is_show_actor = !this.is_show_actor;
          // console.log(res)
          this.my_actors = res.data.my_actor_list
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
        url: `http://127.0.0.1:8000/accounts/${this.Itisme_id}/likethisactor/${my_actor_id}/`,
        headers: this.setToken(),
        data: {
          is_put: this.is_is_put
        }
      })
        .catch(err => {
          console.log(err)
        })
    },
    just_for_fun: function (wow,one=0,two=0) {
      // console.log(this.calar, wow)
      const r = document.querySelector(':root');
      if (wow) {
        r.style.setProperty('--bg-calar', 'linear-gradient('+this.bg_calar[0]+', '+this.bg_calar[1]+', '+this.bg_calar[2]+')')
        console.log(this.bg_calar)
      } else {
        r.style.setProperty('--calar', this.calar)
        one=two
        two=one
      }
    }
  },
  created: function () {
    this.Itisme = localStorage.getItem('Itisme')
    this.Itisme_id = localStorage.getItem('Itisme_id')
    this.getReview()
    // this.just_for_fun(true)
    // this.just_for_fun(false)
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=IM+Fell+French+Canon+SC&display=swap');

:root {
  --bg-calar: linear-gradient(rgb(38, 39, 39),rgb(38, 39, 39),rgb(38, 39, 39));
  --calar: white;
}

input[type="checkbox"]{
  filter:invert(0%) hue-rotate(138deg) brightness(1.9);
  width: 18px;
  height: 18px;
}
.chk{
  background-color: rgb(138, 128, 128);
}
/* body{
  font-weight: ;
} */
#MyProfile{
  background: var(--bg-calar);
  color: var(--calar);
  height: 100vh;
/* background: linear-gradient(rgb(110, 110, 110),rgb(197, 195, 195))} */
  /* background-color:#f5f5dc; */
  /* background: linear-gradient(rgb(17, 17, 17),rgb(28, 28, 31),   rgb(31, 31, 32),rgb(25, 25, 27),rgb(17, 17, 17)); */
}



</style>