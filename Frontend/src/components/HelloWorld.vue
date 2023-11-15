<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import logomarca from '../assets/logomarca.png'
import NavigationPrincipal from './NavigationPrincipal.vue'

const course = ref([]);


const getCourse = async () => {
   const response = await axios.get('http://localhost:3000/api/curso/')
   const result = response.data
   console.log(result)

}

onMounted(() => {
  getCourse()
})

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
