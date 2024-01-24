<script setup>
import { RouterLink } from 'vue-router';	
</script>

<template>
<nav>
<RouterLink to="/">Inicio</RouterLink>
<RouterLink to="/registroestudiante">Registro de Estudiante</RouterLink>
<RouterLink to="/iniciosesion">Inicio Sesion</RouterLink>
</nav>
</template>

<style scoped>
nav {
  font-size: 15px;
  text-align: center;
  border: 4px;
  border-radius: 36px;
  border-style: solid;
  padding: 10px;
  width: 60%;
  border-color: blue;
  background-color: lightblue;
  
}


nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

</style>