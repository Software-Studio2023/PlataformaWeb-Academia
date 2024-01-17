<script setup>
import NavigationPrincipal from './NavigationPrincipal.vue'

</script>
<template>
  <header>
    <NavigationPrincipal />
  </header>
   <body>
    <h1>Software Studio</h1>
      <section class="inicio">
          <h2 class="title1">¿Quienes somos?</h2>
          <p class="contexto">Somos una empresa orientada al aprendizaje en el mundo de la programacion y bases de datos
            , a traves de cursos que se relizan de forma presenciañ con el objetivo de dar las herramientas
            necesarias a las personas, para impulsar el avance tecnologico.
          </p>
          <img src="../assets/logomarca.png">
      </section>

      <section class="cursos">
        <h2 class="title2">Cursos</h2>
        <p>Somos una empresa orientada al aprendizaje en el mundo de la programacion y bases de datos
            , a traves de cursos que se relizan de forma presenciañ con el objetivo de dar las herramientas
            necesarias a las personas, para impulsar el avance tecnologico.</p>
      </section>

      <section class="trabajos">
        <h2>Trabajos realizados</h2>
        <p>Somos una empresa orientada al aprendizaje en el mundo de la programacion y bases de datos
            , a traves de cursos que se relizan de forma presenciañ con el objetivo de dar las herramientas
            necesarias a las personas, para impulsar el avance tecnologico.</p>
      </section>
      
      <footer>
        <h2>Derechos autor Software Studio 2023</h2>
      </footer>
   </body>
</template>

<style scoped>
*{
  margin: 1%;
}


header{
  align-items: center;
  justify-content: center;
  display: flex;
}

h1{
  font-weight: 500;
  font-size: 75px;
  color: blue;
  text-align: center;
}

.inicio{
  padding:0px;
  margin: 0px;
  text-align: justify;
  margin-right: 300px;
  margin-left: 20px;
  background-color: cyan;
  border-style: solid;
  border-top-right-radius: 15px;
  border-bottom-right-radius: 15px;
  border-color: blue;
  display: flex;
}
.contexto{
  margin-right: 20px;
  font-size: 20px;
  align-items: center;
  justify-content: center;
}

img{
  width: 100px;
  height: 100px;
}

.cursos{
  background-color: blue;
  color: white;
  border-style: solid;
  border-color: black;
  margin-left: 300px;
  margin-right: 20px;
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
}
 .trabajos{
  text-align: left;
  width: 1200px;
 }

</style>
