<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'Brg',
  props: {
    personName: {
      type: String,
    }
  },
  methods: {
    gotoprofile: function (personName) {
      const Itisme = localStorage.getItem('Itisme')// 내이름 들고 와서
      if (personName === Itisme) {   // 내이름이랑 함수에서 보내준 이름이랑 같으면? 
        this.$router.push({ name: 'MyProfile' }) //내 프로필로 보낸다 
      } else {  // 다르다면?
        
        this.$router.push({ name: 'Profile', params: { personName, me: this.Itisme } })
      }
    }
  },
  created: function () {
    this.gotoprofile(this.personName)
  }
}
</script>

<style>

</style>