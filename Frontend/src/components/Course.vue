<script setup>
import Navigation from './Navigation.vue'
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';
import {ref, onMounted} from 'vue';

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
    <Navigation/>
    <h1></h1>
</template>