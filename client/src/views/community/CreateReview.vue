<template>
  <div id="createReview">
    <div>
    <br>
    <h1 style=" font-size:500%; font-family: 'IM Fell French Canon SC', serif;" >CREATE</h1>
    <br>
    <label for="">제목:&ensp;</label>
    <input type="text" v-model="review.title" >
    <br><br>
    <hr><br>
    <label for="">평점:&ensp; </label>

    <select v-model="review.rank">
      <option disabled value="">별점을 주세요</option>
      <option value="1">★</option>
      <option value="2">★★</option>
      <option value="3">★★★</option>
      <option value="4">★★★★</option>
      <option value="5">★★★★★</option>
    </select>

    <br><br>
    <hr><br>
    <label for="" style="font-weight:bold">내용 </label>
    <br><br>
    <textarea name="content" id="" v-model="review.content" cols="30" rows="10"></textarea>
    <br><br>
    <v-btn class="mx-2" fab dark color="indigo"  @click="createReview()">
      <v-icon dark>mdi-plus</v-icon>
    </v-btn>
    <!-- <button class="v-btn" style="font-weight:bold">리뷰 등록</button> -->
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'CreateReview',
  data: function (){
    return {
      review:{
        rating: 4,
        title : null,
        rank : null,
        content : null,
        movie_id: localStorage.getItem('movie_id'),
        me: localStorage.getItem('Itisme'),
      },
      my_method : 'post',
      is_put: ''
    }
  },
  params: {
    update_review : {
      type : Object
    },
    for_update: {
      type : Boolean
    },
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview: function () {
      const new_review = this.review
      if (new_review.title ) { // 비지 않았으면
        if (new_review.rank) {
          if (new_review.content) {
            // 다 채운상태
            axios({
              method:`${this.my_method}`,
              url: `http://127.0.0.1:8000/community/create_review/${this.is_put}`,
              headers: this.setToken(),
              data: {
                new_review
              }
            })
              .then(res=>{
                console.log(res)
                if (res.data.already_writen) {
                  alert('이미 이 영화에 남긴 리뷰가 있습니다!')
                  localStorage.setItem('review_id', res.data.new_id)
                  this.$router.push({ name: 'DetailReview'})
                } else {
                localStorage.setItem('review_id', res.data.new_id)
                this.$router.push({ name: 'DetailReview'})
                }
              })
              .catch(err=>{
                console.log(err)
              })
          } else {
            alert('내용 채우셈')
          }
        } else {
          alert('평점 채우셈')
        }
      } else {
        alert('제목 채우셈')
      }
      this.review.title = null
      this.review.rank = null
      this.review.content = null
    }
  },
  created: function() {
    if (this.$route.params.update_review.title){
      this.review.title = this.$route.params.update_review.title
      this.review.content = this.$route.params.update_review.content
      this.review.rank = this.$route.params.update_review.rank
      this.my_method = 'put'
      this.is_put = `update_delete/${this.$route.params.update_review.id}/`
    }
  }
}
</script>
<style scpoed>
  input{ border: 1px solid white;background-color: #ffffff;  border-radius: value;}
  select{ border: 1px solid white;background-color: #ffffff;  border-radius: value;}
  textarea{ border: 1px solid white; background-color: #ffffff; border-radius: value;}
  #createReview{
    height: 100vh;
    font-weight:700;
    background-color:#ece6cc ;
    color: black;
  }
</style>
