<template >
  <div> 
    <h1 class="my-2" style="color:white; font-size:500%; font-family: 'IM Fell French Canon SC', serif;">Detail</h1>

    <!-- <p style="font-size:60px" class="my-5">Detail</p> -->
    <!-- {{review}} -->
    <!-- 생성일시, 수정일시 시간 표기 바꾸기 -->
    <!-- 이건 탭키입니다. -->
    <div id=DetailReview style="background-color:#ece6cc; 
    color:black">
    <br>
    <div >
      <h1 style="font-weight:700">제목 : {{review.title}}</h1>
    </div>
    <div v-if="mine" class="update_delete" >
      <button class="btn btn-warning" @click="update_review">게시글 수정  </button> &nbsp; 
      <button class="btn btn-info" @click="confirmDeleteReview">게시글 삭제</button>
    </div>
    <hr>
    <h3 style="font-weight:700">영화 제목 : {{review.movie}}</h3>
    <p>평점 : {{review.rank}}</p>
    <p>글쓴이 : 
      <span style="cursor:pointer"
        @click="goProfile(review.user)"> 
        {{review.user}}
      </span>
    </p>
    <p>내용 : {{review.content}}</p>
    <div class="date">
      <!-- <p>생성일시 : {{moment(review.created_at.getTime()).add("-3","h").format("HH시 mm분 ss초")}}</p> -->
      <!-- <span>{{ review.created_at | moment("from", "now", true) }}</span> -->
      <p><span>작성: {{ review.created_at | moment("from", "now", true) }} ago</span></p>
      <p><span>수정: {{ review.updated_at | moment("from", "now", true) }} ago</span></p>
    </div>
    <hr>
    <div class='like'>
      <button @click="likeReview" v-if="liked" style="font-size:30px;color:hotpink"><i class="far fa-heart"></i></button>
      <button @click="likeReview" v-if="!liked" style="font-size:30px;"><i class="fas fa-heart"></i></button>
    </div>

    <p>{{ like_count }}명이 좋아합니다!</p>
    <h4 style="cursor:pointer" @click="handle_toggle"> 
      좋아요를 누른 사람들 
      <span v-show="!is_show">▼</span>
      <span v-show="is_show">▲</span>
    </h4>
    <div v-show="is_show" >
      <div v-for="liker in like_users" :key="liker.id">
        {{ liker.username }}
      </div>
    </div>
  
    <hr>
    <div v-if="comments.length > 0">
      <h3>Comments</h3>
      <ul v-for="comment in comments" :key="comment.id">
        <li>{{ comment.user.username }}: {{ comment.content }}
        <button v-show="comment.user.username===Itisme" @click="really(comment.id)" 
         style="color:skyblue">
          <i class="far fa-trash-alt"></i>
        </button></li>
      </ul>
    </div>
    <div v-else>
      <h3 style="font-weight:700">등록된 댓글이 없습니다.</h3>
    </div>
    <div>
      <input @keyup.enter="createComment" type="text" v-model="new_comment_text" placeholder="잘 읽었습니다!"> &nbsp;
      <button @click="createComment" class="btn btn-info">등록</button> 
    </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue' 
import vueMoment from 'vue-moment' 
Vue.use(vueMoment)

import axios from 'axios'
export default {
  name: 'DetailReview',
  data: function () {
    return {
      is_show:false,
      review: {
        id: null,
        title: null,
        content: null,
        created_at: null,
        updated_at: null,
        rank: null,
        movie: null,
        user: null,
      },
      review_id: localStorage.getItem('review_id'),
      liked: false,
      like_count: 0,
      like_users: [],
      mine: false,
      my_comment: false,
      comments: [],
      new_comment_text: null,
      Itisme: localStorage.getItem('Itisme')
    }
  },
  methods: {
    handle_toggle: function(){
      this.is_show = !this.is_show;
      // console.log(moment(d.getTime()).add("-3", "h").format("HH시 mm분 ss초"));
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    goProfile: function (personName) {
      // console.log(personName)
      this.$router.push({ name: 'Brg', params: { personName, me: localStorage.getItem('Itisme') } })
      this.personName = null
    },
    getDetailReview: function () {
      // const review_id = localStorage.getItem('review_id')
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.review_id}/`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          const Itisme = localStorage.getItem('Itisme')
          this.review.id = res.data.id
          this.review.title = res.data.title
          this.review.content = res.data.content
          this.review.movie = localStorage.getItem('movie_name')
          this.review.rank = res.data.rank
          this.review.created_at = res.data.created_at
          this.review.updated_at = res.data.updated_at
          this.review.user = res.data.user.username
          this.like_count = res.data.like_users.length
          this.like_users = res.data.like_users
          this.getComment()
          this.like_users.forEach(element => {
            if (element.username === Itisme) {
              this.liked = true
            }
          })
          if (Itisme===this.review.user) {
            this.mine = true
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    likeReview: function () {
      // const review_id = localStorage.getItem('review_id')

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.review_id}/like_review/`,
        headers: this.setToken()
      })
        .then(res => {
          const Itisme = localStorage.getItem('Itisme')
          // console.log(res)
          this.liked = res.data.liked
          this.like_count = res.data.like_count
          if (this.liked) {
            this.like_users.push({'username': `${Itisme}`})
          } else {
            const my_idx = this.like_users.indexOf(`${Itisme}`)
            this.like_users.splice(my_idx, 1)
          }
          // 버그를 잡기위해서 서버의 폭발은 고려하지 않음.
          this.getDetailReview()
          // this.getDetailReview()
          // this.like_users = res.data.like_users
        })
        .catch(err => {
          console.log(err)
        })
    },
    update_review: function () {
      this.$router.push({name: 'CreateReview', params: {update_review: this.review, for_update: true} })
    },
    delete_review: function () {
      axios({
        method:`delete`,
        url: `http://127.0.0.1:8000/community/create_review/update_delete/${this.review_id}`,
        headers: this.setToken(),
      })
        .then(res=>{
          console.log(res)
          this.$router.push({ name: 'ReviewIndex' })
        })
        .catch(err=>{
          console.log(err)
        })
    },
    createComment: function () {
      axios({
        method:`put`,
        url: `http://127.0.0.1:8000/community/create_delete_comment/${this.review_id}/`,
        headers: this.setToken(),
        data:{
          comment: this.new_comment_text,
          me: localStorage.getItem('Itisme_id')
        },
      })
        .then(res=>{
          console.log(res)
          this.getComment()
          this.new_comment_text = null
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getComment: function () {
      axios({
        method:`post`,
        url: `http://127.0.0.1:8000/community/get_comment/${this.review_id}/`,
        headers: this.setToken(),
      })
        .then(res=>{
          console.log(res)
          this.comments = res.data
        })
        .catch(err=>{
          console.log(err)
        })
    },
    deleteComment: function(comment_id) {
      axios({
        method:`delete`,
        url: `http://127.0.0.1:8000/community/create_delete_comment/${comment_id}/`,
        headers: this.setToken(),
      })
        .then(res=>{
          console.log(res)
          this.getComment()
        })
        .catch(err=>{
          console.log(err)
        })
    },
    really: function (comment_id) {
      if (confirm("정말 이 댓글을 삭제하실 건가요?") == true){
        this.deleteComment(comment_id)
      } else {
        return
      }
    },
    confirmDeleteReview: function () {
      if (confirm("정말 이 리뷰를 삭제하실 건가요?") == true){
        this.delete_review()
      } else {
        return
      }
    },
  },
  created: function () {
    this.getDetailReview()
  },
}
</script>

<style scoped>
  .date > p{
    text-align: center;
    font-size:15px
  }
  .like >button{
    border: none;
    outline:none;
  }
  #DetailReview{
    height: 100vh;
    font-weight:700
  }
</style>