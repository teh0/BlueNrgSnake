<template>
  <Snake/>
</template>

<script>
import Snake from "./components/Snake.vue";

export default {
  components: {
    Snake
  }
}

</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;700&display=swap');
  #app {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-family: 'Work Sans', sans-serif;
  }
</style>