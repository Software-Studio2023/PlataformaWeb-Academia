<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import CreateStudents from './CreateStudents.vue';

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
  <div class="greetings">
   <h1>Software Studios</h1>
  </div>
  <CreateStudents/>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: static;
  top: -10px;
  color: blue;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
