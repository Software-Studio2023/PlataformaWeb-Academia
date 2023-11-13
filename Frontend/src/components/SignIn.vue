<template>
 <div>
 	<h1>Inicio Sesión</h1>
 <form>
   <label for="studentsEmail">Email</label>
    <input type="text" id="stundentsEmail" v-model="studentsEmail" required>
     <label for="studentsRol">Contraseña</label>
     <input type="text" id="studentsRol" v-model="studentsRol" required>
    <button type="submit">Enviar</button>
</form>
 </div>
</template>

