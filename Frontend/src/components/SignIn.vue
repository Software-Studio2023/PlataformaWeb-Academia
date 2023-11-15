<template>
 <div>
 <h1>Inicio Sesión</h1>
 <form @submit.prevent="signIn">
   <label for="studentsEmail">Email</label>
    <input type="text" id="stundentsEmail" v-model="studentsEmail" required>
     <label for="studentsPassword">Contraseña</label>
     <input type="text" id="studentsPassword" v-model="studentsPassword" required>
    <button type="submit">Enviar</button>
</form>
 </div>
</template>

<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const studentsEmail = ref('');
const studentsPassword = ref('');
const store = useStore();
const router = useRouter();

const signIn = () => {

store.dispatch('login', {
	email: studentsEmail.value,
	password: studentsPassword.value
})

.then(()=>{
   router.push('/dashboard')
})

}

</script>