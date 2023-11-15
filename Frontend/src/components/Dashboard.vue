<script setup>
import { ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import Navigation from './Navigation.vue'
import axios from 'axios';

const welcomeMessage = ref('')
const store = useStore()

const getIdStudent = async () => {
  const studentname = store.state.namestudent
  welcomeMessage.value = studentname
}

onMounted(() => {
 getIdStudent()
})

</script>


<template>
    <Navigation/>
    <h1>Bienvenido {{ welcomeMessage }}</h1>
</template>



