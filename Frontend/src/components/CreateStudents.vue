<template>
    <div>
        <h1>Registro de Usuario</h1>
        <form @submit.prevent="CreateStudents">

           <label for="studentsName">Nombre</label>
           <input type="text" id="studentsName" v-model="studentsName" required>
           
           <label for="studentsLastname">Apellido</label>
           <input type="text" id="studentsLastname" v-model="studentsLastname" required>
           
           <label for="studentsEmail">Email</label>
           <input type="text" id="stundentsEmail" v-model="studentsEmail" required>

           <label for="studentsRol">Indique su Rol</label>
           <input type="text" id="studentsRol" v-model="studentsRol" required>

           <label for="studentsPassword">Contraseña</label>
           <input type="password" id="studentsPassword" v-model="studentsPassword" required>
            <button type="submit">Enviar</button>
        </form>
    </div>
</template>

<script setup>
    import Swal from 'sweetalert2';
    import  {VueElement, ref} from 'vue';
    import axios from 'axios';
    
    const studentsName = ref("");
    const studentsLastname = ref("");
    const studentsEmail = ref("");
    const studentsRol = ref("");
    const studentsPassword = ref("")

    const CreateStudents = async() => {
        const response = await 
        axios.post('http://localhost:3000/api/students/', { name:studentsName.value, lastname:studentsLastname.value, email:studentsEmail.value, rol:studentsRol.value, password:studentsPassword.value})
        confirmAlert()
    }
    const confirmAlert = () => {
        Swal.fire({
            icon: 'success',
            title: 'Registrado Exitosamente',
            text: 'Inicia sesion para poder acceder a nuestro cursos'
        })
    }
</script>