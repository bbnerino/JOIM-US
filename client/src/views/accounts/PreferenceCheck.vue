<template>
  <div class="select">
    <br>
    <h1 style="font-weight:600">좋아하는 배우를 골라주세요♥</h1><br>
    <p>이 선택은 만든다. 당신의 추천페이지 더 완벽</p>
    <div class="container">
      <div class="row">
        <div class="col-3" v-for="actor in actors" :key="actor.id">
          <img style="border-radius:35%; margin-top:20px" 
  
          :src="`${URL + actor.profile_path}`" alt="profile_path" width=50%>
          <h2 style="font-weight:500" >{{ actor.name }} 
          <br>

          <input type="checkbox" :value="`${actor.actor_id}`" 
          :id="`${actor.actor_id}`" v-model="checked_actors" 
          @change="changedLike(actor.actor_id)"></h2>
        </div>
      </div>
    </div>
    <br>
    <div class="row">
      <span class="offset-3 col-2" v-show="page_num === 0"></span>
      <button class="offset-3 col-2 btn btn-primary" 
        @click="setActorPage(-1)" v-show="page_num >0" >이전</button>
      
      <button class="offset-2 col-2 btn btn-primary" @click="setActorPage(+1)">다음</button>
      <!-- <button class="offset-1 col-2 btn btn-danger" @click="really">그만하기</button> -->
      
      <button class="offset-1 col-2 btn btn-danger" data-toggle="modal" data-target="#exampleModalCenter">
        그만하기
      </button>
    </div>
<!-- 모달 -->
<div class="modal fade" id="exampleModalCenter" 
tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" 
aria-hidden="true" >
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 style="color:black" class="modal-title" id="exampleModalLongTitle">그만하기</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" style="color:black">
        배우 추가를 그만두시겠습니까?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-info" data-dismiss="modal">더하기</button>
        <button type="button" class="btn btn-danger" data-dismiss="modal"  @click="really">끝내기</button>
      </div>
    </div>
  </div>
</div>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PrefrenceCheck',
  data: function () {
    return {
      all_actors: [],
      actors: [],
      checked_actors: [],
      is_is_put: null,
      page_num: 0,
      URL: 'https://image.tmdb.org/t/p/w500/',
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
    getActors: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/getactorsforcheck/`,
        headers: this.setToken(),
      })
      .then(res => {
          console.log(res)
          this.all_actors = res.data
          this.setActorPage()
        })
        .catch(err => {
          console.log(err)
        })
    },
    changedLike: function(my_actor_id) {
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
    setActorPage: function (is_back=0) {
      this.page_num = this.page_num + is_back
      
      this.actors = this.all_actors.slice(this.page_num * 8 , (this.page_num + 1) * 8)
      
    },
    really: function () {
        this.$router.push({name: 'LogBrg'})
    },
  },
  created: function () {
    this.getActors()
  },
}
</script>


<style scoped >
  .avatar {
  vertical-align: middle;
  width: 50px;
  height: 50px;
  border-radius: 50%;
}
</style>