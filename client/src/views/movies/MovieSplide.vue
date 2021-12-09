<template>
<div>

  <swiper class="swiper" :options="swiperOption">
  
    <swiper-slide ><img @click="detailMovie(MOVIES['토이스토리'])" src="@/img/토이스토리.jpg" alt=""></swiper-slide>
    <swiper-slide ><img @click="detailMovie(MOVIES['심슨'])" src="@/img/심슨.jpg" alt=""></swiper-slide>
    <swiper-slide ><img @click="detailMovie(MOVIES['위더베어스'])" src="@/img/위더베어스.jpg" alt=""></swiper-slide>
    <swiper-slide ><img @click="detailMovie(MOVIES['겨울왕국'])" src="@/img/겨울왕국.jpg" alt=""></swiper-slide>
    <swiper-slide ><img @click="detailMovie(MOVIES['코코'])" src="@/img/코코.jpg" alt=""></swiper-slide>
    <swiper-slide ><img @click="detailMovie(MOVIES['너의이름은'])" src="@/img/너의이름은.jpg" alt=""></swiper-slide>
    <swiper-slide ><img @click="detailMovie(MOVIES['피터레빗'])" src="@/img/피터레빗.jpg" alt=""></swiper-slide>
    <swiper-slide ><img @click="detailMovie(MOVIES['소울'])" src="@/img/소울.jpg" alt=""></swiper-slide>
    
    <div class="swiper-pagination swiper-pagination-white" slot="pagination"></div>
    <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>
    <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
  </swiper>

  <!-- 첫번째 슬라이드 --> 

  <p style="opacity:0.7;text-align:left;margin-left:10px">{{reco_genre_one}}</p>
  <div class="example-3d">
    <swiper class="swiper_1" :options="swiperOption_2">
      <swiper-slide><img @click="detailMovie(recommended_movies_one[0])" :src="`${URL + recommended_movies_one[0].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[1])" :src="`${URL + recommended_movies_one[1].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[2])" :src="`${URL + recommended_movies_one[2].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[3])" :src="`${URL + recommended_movies_one[3].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[4])" :src="`${URL + recommended_movies_one[4].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[5])" :src="`${URL + recommended_movies_one[5].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[6])" :src="`${URL + recommended_movies_one[6].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[7])" :src="`${URL + recommended_movies_one[7].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[8])" :src="`${URL + recommended_movies_one[8].poster_path}`" alt=""></swiper-slide>
      <swiper-slide><img @click="detailMovie(recommended_movies_one[9])" :src="`${URL + recommended_movies_one[9].poster_path}`" alt=""></swiper-slide>
      <div class="swiper-pagination" slot="pagination_2"></div>
    </swiper>
  </div>

 <!-- 두번째 슬라이드 -->
 <p style="opacity:0.7;text-align:left;margin-left:10px">{{reco_genre_two}}</p>
  <div class="example-3d">
    <swiper class="swiper_1"    :options="swiperOption_1"> 
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[0])" :src="`${URL + recommended_movies_two[0].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[1])" :src="`${URL + recommended_movies_two[1].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[2])" :src="`${URL + recommended_movies_two[2].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[3])" :src="`${URL + recommended_movies_two[3].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[4])" :src="`${URL + recommended_movies_two[4].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[5])" :src="`${URL + recommended_movies_two[5].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[6])" :src="`${URL + recommended_movies_two[6].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[7])" :src="`${URL + recommended_movies_two[7].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[8])" :src="`${URL + recommended_movies_two[8].poster_path}`" alt=""></swiper-slide>
      <swiper-slide class="ho"><img @click="detailMovie(recommended_movies_two[9])" :src="`${URL + recommended_movies_two[9].poster_path}`" alt=""></swiper-slide>
      <div class="swiper-pagination" slot="pagination_1"></div>
    </swiper>
  </div>
  
  
</div>  
</template>

<script lang="ts">
import axios from 'axios';
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";
export default{
  name:'MovieSplide',
  props:{
    recommended_movies_one:Object,
    recommended_movies_two:Object,
    reco_genre_one:String,
    reco_genre_two:String
  },
  components: {
    Swiper,
    SwiperSlide
  },
  data() {
      return {
        URL: 'https://image.tmdb.org/t/p/w500/',
        MOVIES: {
          '토이스토리': {id:314},
          '심슨':{id:340},
          '위더베어스':{id:395},
          '겨울왕국':{id:242},
          '코코':{id:90},
          '너의이름은':{id:261},
          '피터레빗':{id:177},
          '소울':{id:145},
        },
        swiperOption: {
          spaceBetween: 30,
          effect: 'fade',
          loop: true,
          autoplay: {
            delay: 2500,
            disableOnInteraction: false,
          },
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },

        swiperOption_1: {
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 'auto',
          loop: true,
          coverflowEffect: {
            rotate: 0,
            stretch: 10,
            depth: 0,
            modifier: 1,
            slideShadows : true
          },
          autoplay: {
            delay: 1500,
            disableOnInteraction: false,
            // pauseOnMouseEnter:true,
            reverseDirection:false,
            // reverse:true
          },
          pagination_1: {
            el: '.swiper-pagination'
          }
      },

      swiperOption_2: {
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 'auto',
          loop: true,
          coverflowEffect: {
            rotate: 0,
            stretch: 10,
            depth: 0,
            modifier: 1,
            slideShadows : true
          },
          autoplay: {
            delay: 1500,
            disableOnInteraction: false,
            pauseOnMouseEnter:true,
            reverseDirection:true,
          },
          pagination_2: {
            el: '.swiper-pagination'
          }
      },
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
    idDetailMovie:function(movie_id){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie_id}/`,
        headers: this.setToken()
      })
        .then(res=>{
          console.log(res)
          this.$router.push({name:'DetailMovie'})
        })
        .catch(err=>{
          console.log(err)
        })
    },
    detailMovie: function (movie) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          localStorage.setItem('movie_id',res.data.id)
          localStorage.setItem('movie_title', res.data.title)
          localStorage.setItem('movie_overview', res.data.overview)
          localStorage.setItem('movie_poster_path', res.data.poster_path)
          this.$router.push({ name: 'DetailMovie'})
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {}
}
</script>

<style lang="scss" scoped>

  .example-3d {
    width: 100%;
    height: 100%;
    // height: 400px;
    // padding-top: 50px;
    padding-bottom: 20px;
  .swiper_1 {
    height: 100%;
    width: 100%;

    .swiper-slide {
      display: flex;
      justify-content: center;
      align-items: center;
      // width: 100%;
      // height: 50%;
      width: 300px;
      height: 450px;
      text-align: center;
      font-weight: bold;
      font-size:100px;
      background-color: #2C8DFB;
      background-position: center;
      background-size: cover;
      color: white;
      img{
        width: 300px;
        height: 450px;

      }
      .swiper-pagination {
         .swiper-pagination-bullet.swiper-pagination-bullet-active {
        background-color: white;
      }
    }
  }}}
  .swiper_2{
    height: 100%;
    width: 100%;

    .swiper-slide {
      display: flex;
      justify-content: center;
      align-items: center;
      // width: 100%;
      // height: 50%;
      width: 919px;
      height: 383px;
      text-align: center;
      font-weight: bold;
      font-size:100px;
      background-color: #2C8DFB;
      background-position: center;
      background-size: cover;
      color: white;
      img{
        width: 300px;
        height: 450px;
      }
      .swiper-pagination {
         .swiper-pagination-bullet.swiper-pagination-bullet-active {
        background-color: white;
      }
    }
  }}
  .swiper {
    height: 100%;
    width: 80%;
    padding-top: 20px;
    padding-bottom: 20px;
    .swiper-slide {
      background-position: center;
      background-size: cover;
      img{
        cursor:pointer;
        width:1700px;
        height: 700px;
        // 0.7배
        // width: 1366px;
        // height: 768px;
      }
    }
  }

  div{
    .swiper{
      .swiper-slide:hover .ho{
        transform: scale(1.1);
        transition: 0.8s;
      }
    }
  }

</style>