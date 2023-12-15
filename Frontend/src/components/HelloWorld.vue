<script setup>
import logomarca from '../assets/logomarca.png'
import NavigationPrincipal from './NavigationPrincipal.vue'

</script>

<template>
  <div>
    <NavigationPrincipal />
   <h1>Software Studio</h1>
   </div>
   <div  class="greetings">
   <img :src="logomarca" />
 </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: static;
  top: -10px;
  color: blue;
  text-align: center;
}

p{
  text-align: center;
  color: blue;
  font-weight: 500;
}

h3 {
  font-size: 1.2rem;
}



.greetings{
  display: flex;
  justify-content: center;
}

</style>
