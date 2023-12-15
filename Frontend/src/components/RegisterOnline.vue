<template>
<div>
  <h1>Registro en Linea</h1>
  <form @submit.prevent="RegisterOnline">
           <label for="registerName">Nombre</label>
           <input type="text" id="registerName" v-model="registerName" required>
           
           <label for="registerLastname">Apellido</label>
           <input type="text" id="registerLastname" v-model="registerLastname" required>
           
           <label for="registerCI">Cédula</label>
           <input type="text" id="registerEmail" v-model="registerCI" required>

           <label for="registerPhone">Teléfono</label>
           <input type="text" id="registerPhone" v-model="registerPhone" required>

           <label for="registerEmail">Correo</label>
           <input type="text" id="registerEmail" v-model="registerEmail" required>

            <label for="registerCourse">Curso</label>
           <input type="text" id="registerCourse" v-model="registerCourse" required>

           <label>¿Como Nos Contacto?</label>
            <input type="text"   v-model="registerContact"/>
           <input type="checkbox" value="Instagram"  v-model="registerContact"/>
           <label>Instagram</label>
           <input type="checkbox"  value="Facebook" v-model="registerContact"/>
           <label>Facebook</label>
           <input type="checkbox" value="Recomendacion" v-model="registerContact"/>
           <label>Recomendación</label>
           <input type="checkbox" value="Otros" v-model="registerContact"/>
           <label>Otros</label>
            <button type="submit">Enviar</button>
        </form>
        <span>Opcion: {{ registerContact }}</span>
  </div>
</template>


<script setup>

import {ref} from 'vue';
import axios from 'axios';

const registerName = ref('')
const registerLastname = ref('')
const registerCI = ref('')
const registerPhone = ref('')
const registerEmail = ref('')
const registerCourse = ref('')
const registerContact = ref('')
//const registerContact = ref([])

const RegisterOnline = async() => {
 const response = await axios.post('http://localhost:3000/api/registeronline/', {name: registerName.value, lastname: registerLastname.value, ci: registerCI.value, phone: registerPhone.value, email: registerEmail.value, course: registerCourse.value, contact: registerContact.value})
 console.log(response)
}


</script>