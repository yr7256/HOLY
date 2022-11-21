<template>
  <section class="wrap" @click="toMainPage">
    <div class="box">
      <img class="test" src="../assets/intro.png" alt="">
    </div>
    <div class="box">
      <img class="test" src="../assets/intro.png" alt="">
    </div>
    <div class="circle"></div>
  </section>
</template>

<script>
export default {
  name : 'IntroPage',
  methods : {
    toMainPage : function(){
      this.$router.push({name : 'MovieView' })
    }
  }
}

const html = document.documentElement

html.addEventListener("mousemove", function(e) {    
  html.style.setProperty('--x', e.clientX + 'px')
  html.style.setProperty('--y', e.clientY + 'px')
})

window.addEventListener("load", function(){
  html.style.setProperty('--x', 0)
  html.style.setProperty('--y', 0)
})

</script>

<style scoped>


.wrap,
.box {
  position: absolute;
  top: 0;
  left: 0;
  width:100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: url('../assets/back.jpg');
  background-size: cover;       
  background-position: center;  
  background-attachment: fixed; 
  overflow: hidden; 
  z-index: 1500;
}

.test {
  height: 80vh;
}

.box:nth-child(1) {
  filter: blur(10px);     
}

.box:nth-child(2) {
  clip-path: circle(120px at var(--x) var(--y));
}


.circle {
  position: absolute;
  width: 240px;
  height: 240px;
  border: 2px solid white;
  border-radius: 50%;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  top: -120px;
  left: -120px;
  transform: translate(var(--x),var(--y));
  z-index: 1600;
}
</style>